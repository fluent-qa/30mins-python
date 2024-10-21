#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd


class JmeterAnalyser:

    def __init__(self, result_file_path: str):
        self.result = {}
        self.prompts = {}
        self.df = None

    def load(self, csv_file: str):
        self.df = pd.read_csv(csv_file)

    def __result_config(self):
        result = {
            "Latency": [{"avg_rt", "avg"}, {"avg_90"}]
        }

    """
    1. generate standard performance result
    2. generate importance metrics
    """

    def generate_performance_data(self):
        avg_idle_time = self.df["IdleTime"].mean()
        avg_rt_time = self.df["Latency"].quantile([0.5, 0.9, 0.95])
        print(dir(self.df["Latency"]))
        print(self.df.head())
        print(self.df.describe()['Latency'])
        print(avg_idle_time, avg_rt_time)

        rt_sets = {
            "max": self.df.describe()['Latency']["max"],
            "min": self.df.describe()['Latency']["min"],
            "平均": self.df.describe()['Latency']["mean"],
            "90%": self.df["Latency"].quantile(0.9),
            "95%": self.df["Latency"].quantile(0.95),
            "std": self.df.describe()['Latency']["std"]
        }
        print(rt_sets)
        """
        从这组数据来看，这个API可能存在的性能问题是响应时间的方差较大，标准差较高，最大响应时间较长。这可能意味着在某些情况下，
        API的响应时间会非常慢，导致用户体验不佳。建议进一步分析API的性能瓶颈，找出问题所在并进行优化。
        """

    def generate_prompts(self):
        pass

    def get_result_analysis(self):
        pass
