class FinancialFreedomCalculator:
    """
    一个用于计算实现财务自由所需时间的类，考虑了多种经济因素。

    Attributes:
        initial_income (float): 初始年收入。
        monthly_expense (float): 每月支出。
        investment_return_rate (float): 投资回报率。
        wage_increase_rate (float): 工资增长率。
        job_hopping_increase_rate (float): 跳槽涨薪比率。
        years_to_hop (int): 多少年跳槽一次。
        inflation_rate (float): 通货膨胀率。
        tax_rate (float): 税率。
        emergency_fund (float): 紧急资金。
    """

    def __init__(self, initial_income, monthly_expense, investment_return_rate, 
                 wage_increase_rate=0.05, job_hopping_increase_rate=0, years_to_hop=0,
                 inflation_rate=0.03, tax_rate=0.2, emergency_fund=0):
        """
        初始化计算器实例。

        Args:
            initial_income (float): 初始年收入。
            monthly_expense (float): 每月支出。
            investment_return_rate (float): 投资回报率。
            wage_increase_rate (float): 工资增长率，默认为5%。
            job_hopping_increase_rate (float): 跳槽涨薪比率，默认为0（不考虑跳槽）。
            years_to_hop (int): 多少年跳槽一次，默认为0（不考虑跳槽）。
            inflation_rate (float): 通货膨胀率，默认为3%。
            tax_rate (float): 税率，默认为20%。
            emergency_fund (float): 紧急资金，默认为0。
        """
        self.initial_income = initial_income
        self.monthly_expense = monthly_expense
        self.investment_return_rate = investment_return_rate
        self.wage_increase_rate = wage_increase_rate
        self.job_hopping_increase_rate = job_hopping_increase_rate
        self.years_to_hop = years_to_hop
        self.inflation_rate = inflation_rate
        self.tax_rate = tax_rate
        self.emergency_fund = emergency_fund

    def calculate_years_to_financial_freedom(self):
        """
        计算实现财务自由所需的年数。

        Returns:
            int: 实现财务自由所需的年数。
        """
        annual_expense = self.monthly_expense * 12
        required_capital = (annual_expense - self.emergency_fund) / (0.04 - self.inflation_rate)
        current_capital = 0
        current_income = self.initial_income
        years = 0

        while current_capital < required_capital:
            net_income = current_income * (1 - self.tax_rate)  # 税后收入
            annual_savings = net_income - annual_expense
            current_capital += annual_savings
            current_capital *= (1 + self.investment_return_rate)
            years += 1

            # 每三年调整一次收入
            if self.job_hopping_increase_rate > 0 and years % self.years_to_hop == 0:
                current_income *= (1 + self.job_hopping_increase_rate)
            else:
                current_income *= (1 + self.wage_increase_rate)

        return years

# 示例：初始年收入45万，月支出1万，投资回报率5%，每三年跳槽一次，跳槽涨薪50%
calculator = FinancialFreedomCalculator(100000, 10000, 0.04, job_hopping_increase_rate=0.0, years_to_hop=3, tax_rate=0.13)
years_to_freedom = calculator.calculate_years_to_financial_freedom()
print(years_to_freedom)
