# 代码生成时间: 2025-09-12 11:03:03
import pandas as pd
import gradio as gr

# 数据清洗和预处理工具
class DataCleaner:
    def __init__(self, df):
        """
        DataCleaner类的初始化函数
        :param df: 待清洗和预处理的DataFrame
        """
        self.df = df

    def remove_duplicates(self):
        """
        移除数据集中的重复行
        :return: 无重复行的DataFrame
        """
        self.df = self.df.drop_duplicates()
        return self.df

    def fill_missing_values(self, strategy):
        """
        填充缺失值
        :param strategy: 填充策略，可以是'mean', 'median', 'mode', 'constant'
        :return: 填充缺失值后的DataFrame
        """
        if strategy == 'mean':
            self.df = self.df.fillna(self.df.mean())
        elif strategy == 'median':
            self.df = self.df.fillna(self.df.median())
        elif strategy == 'mode':
            self.df = self.df.fillna(self.df.mode().iloc[0])
        elif strategy == 'constant':
            self.df = self.df.fillna(0)
        else:
            raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', 'constant'.")
        return self.df

    def convert_to_datetime(self, columns):
        """
        将指定列转换为datetime类型
        :param columns: 包含待转换列名的列表
        :return: 转换后的DataFrame
        """
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        return self.df

    def main(self):
        """
        主函数，用于演示数据清洗和预处理的流程
        """
        # 加载数据集
        data = pd.read_csv('data.csv')

        # 创建DataCleaner实例
        cleaner = DataCleaner(data)

        # 移除重复行
        cleaner.remove_duplicates()

        # 填充缺失值
        cleaner.fill_missing_values('mean')

        # 将指定列转换为datetime类型
        columns_to_convert = ['date', 'timestamp']
        cleaner.convert_to_datetime(columns_to_convert)

        # 保存清洗和预处理后的数据
        cleaner.df.to_csv('cleaned_data.csv', index=False)

if __name__ == '__main__':
    # 定义GRADIO界面
    def clean_and_preprocess(df):
        """
        数据清洗和预处理函数
        :param df: 待清洗和预处理的DataFrame
        :return: 清洗和预处理后的DataFrame
        """
        cleaner = DataCleaner(df)
        cleaner.remove_duplicates()
        cleaner.fill_missing_values('mean')
        columns_to_convert = ['date', 'timestamp']
        cleaner.convert_to_datetime(columns_to_convert)
        return cleaner.df

    # 创建输入输出组件
    input_component = gr.Interface(
        fn=clean_and_preprocess, 
        inputs=pd.DataFrame, 
        outputs=pd.DataFrame,
        title='数据清洗和预处理工具'
    ).launch()
