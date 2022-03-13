"""
A financial ratio or accounting ratio is a relative magnitude of two
selected numerical values taken from an enterprise's financial statements.
Often used in accounting, there are many standard ratios used to try to
evaluate the overall financial condition of a corporation or other
organization.

Info Source:
    https://finance.zacks.com/seven-ways-analyze-stock-4845.html
    https://www.quora.com/What-are-3-most-important-financial-ratios-
        we-should-study-before-investing-in-stocks
    https://www.theinvestorspodcast.com/warren-buffett-investment-strategy/
        module-2/rule-1-leadership/
        #:~:text=To%20be%20sure%20of%20the,as%20expected%20to%20flow%20out.

Data Sources:
    https://finance.yahoo.com/quote/NFLX/financials?p=NFLX
    https://finbox.com/
"""


def gross_profit_margin(gross_profit, total_revenue):
    """
    The gross profit margin measures a company's gross profit as a percentage
    of the revenue. The formula to calculate gross profit margin and an
    example calculation for Apple's trailing twelve months is outlined below:

    Example:
        https://finbox.com/NASDAQGS:AAPL/explorer/gp_margin

        Fiscal Year  Gross Profit  Revenue  Margin
        2017-09-30   88.186 B      229.2 B  38.5%
        2018-09-29   101.8 B       265.6 B  38.3%
        2019-09-28   98.392 B      260.2 B  37.8%
        2020-09-26   105 B         274.5 B  38.2%
        2021-09-25   152.8 B       365.8 B  41.8%

        Gross Profit Margin (%)  = Gross Profit / Total Revenue
        43.0% = $162.8 B / $378.3 B

    Comment:
        Points to the pricing power of a company. Anything higher than 30-35%
        is good enough. Beyond 40% GPM is fantastic. However, a low GPM
        doesn't necessarily indicate a bad company. Industries where
        competition is high, you will struggle to find any company with a
        GPM above 20% even. The same is also true for matured companies.
        But if you are a believer in the Graham-type classic Value Investment,
        you'll avoid any company with a GPM below 30%. For example, I hold
        Raymond Ltd, having a GPM of ~5%, yet it's given me a CAGR of 89%
        until now. This is because Raymond is in a highly fragmented industry
        (Textiles) and is also a matured company. Also refer to #11 and #12
        on why I continue to hold Raymond given the above details. Quora

    Returns:
        TODO: Add returns
    """
    return gross_profit / total_revenue


def operating_profit_margin():
    """
    Operating profit is the total income a company generates from sales after
    paying off all operating expenses, such as rent, employee payroll,
    equipment and inventory costs. The operating profit figure excludes gains
    or losses from interest, taxes and investments.

    Example:
        TODO: Add example

    Comment:
        Points to the operational efficiency of a company. Just because a
        company has pricing power doesn't mean it can run its operations
        efficiently. A 15-20% OPM is good enough. However, if the growth in
        OPM is higher than the growth in GPM, it's a positive sign that the
        company makes up for the inability to price by controlling its costs.
        Look at literally any company which gave a good long term returns and
        you will find their historical OPM on the higher side of the scale.
        Quora

    To implement:
        https://www.americanexpress.com/en-gb/business/
            trends-and-insights/articles/operating-profit-formula/
            #:~:text=The%20operating%20profit%20formula%20is,
            # %2DDay%20Expenses%20%3D%20Operating%20Profit.

    Returns:
        TODO: Add returns
    """
    raise NotImplementedError("Operating profit margin not implemented yet")


def net_profit_margin(total_revenue, cost_of_revenue):
    """
    Profit margin, net margin, net profit margin or net profit ratio is a
    measure of profitability. It is calculated by finding the net profit as a
    percentage of the revenue.

    Example:
        https://finbox.com/NASDAQGS:AAPL/explorer/cor

        Fiscal Year  Cost of Revenues  Revenue  % Revenue
        2017-09-30   141 B             229.2 B  61.5%
        2018-09-29   163.8 B           265.6 B  61.7%
        2019-09-28   161.8 B           260.2 B  62.2%
        2020-09-26   169.6 B           274.5 B  61.8%
        2021-09-25   213 B             365.8 B  58.2%

        Net Profit Margin (%)  = (Revenue - Cost of Revenues) / Revenue
        41.8% = ($365.8 B - $213 B) / $365.8 B

    Comment:
        Shows how efficiently a company handles its financial obligations.
        Anything above 10% is good enough here. But a higher figure isn't
        necessarily good. Say, if the OPM and NPM are almost the same,
        it's a big red flag denoting that the company might be capitalizing
        its interest and/or tax payments. That is not so bad, as long as you
        understand just how much they owe and deduct it from the margin
        (Just to understand the true NPM). If it looks like company has been
        doing it for a long time, you may want to look at the Notes to
        Financials to understand where the Tax and Interest obligations are
        going. Finally, consistency is key in all the Margin-related Ratios.
        It's of no use if only one Ratio is good or if all the Ratios are good
        only for one period. Quora

    Returns:
        TODO: Add returns
    """
    return (total_revenue - cost_of_revenue) / total_revenue


def net_income_via_other_income(net_income, other_income):
    """
    Other income is income that does not come from a company's main business,
    such as interest. Examples of other income include income from interest,
    rent, and gains resulting from the sale of fixed assets.

    Example:
        TODO: Add example

    Comment:
        You wouldn't want a company to consistently earn its Net Income via
        “Other” Income. If this Ratio is above 10%, it's a red flag.
        If it's just a one off item, make sure you look through the Notes
        to Financials to understand what constitutes Other Income. Quora

    Returns:
        TODO: Add returns
    """
    return other_income / net_income


def revenue_depreciation(total_revenue, reconciled_depreciation):
    """
    The term depreciation refers to an accounting method used
    to allocate the cost of a tangible or physical asset over
    its useful life or life expectancy. Depreciation represents
    how much of an asset's value has been used.

    Example:
        TODO: Add example

    Comment:
        Applies only to manufacturing companies or companies with a lot of
        Tangible Assets. Good companies have a very low Depreciation Margin of
        1-2%. A low DpM denotes that the company has invested a lot in Assets
        with a very long useful life and/or Assets which will be worth a lot
        even after years of operation (Scrap value). Raymond has a DpM of
        2.8% (Which is a little off, but acceptable). Quora

    Returns:
        TODO: Add returns
    """
    return reconciled_depreciation / total_revenue


def equity_debt(equity, debt):
    """
    Equity: Equity represents the value that would be returned to a company's
        shareholders if all of the assets were liquidated and all of the
        company'sdebts were paid off. We can also think of equity as a degree
        of residual ownership in a firm or asset after subtracting all debts
        associated with that asset.

    Debt: Debt means the amount of money which needs to be repaid back and
        financing means providing funds to be used in business activities. An
        important feature in debt financing is the fact that you are not
        losing ownership in the company.

    Example:
        TODO: Add example

    Comment:
        A combination of clever management and trusty debtors can steer a
        highly indebted company with ease. However, more often than not,
        it's impossible to find that combination. I personally ignore any
        company with a D/E more than 40%, because pressure from Debtors can
        force the management to focus more on short term profits
        (Translates to interest payments) as opposed to long term growth
        (Translates to Return on Equity). BFSI companies have D/E ranging from
        5-10, which is fine. You can cap the D/E for BFSI companies at 7 or so.
        Raymond has a D/E of 1.06, which is okay, because their Interest
        Coverage is ~1.5. This means that the Cost of Debt is probably very
        low. I also place a lot of trust in their Management.

    Returns:
        TODO: Add returns
    """
    return debt / equity


def interest_coverage(ebit, interest_expense):
    """
    TODO: Implement documentation

    To implement:
        https://finbox.com/NASDAQGS:AAPL/explorer/interest_coverage
        https://www.investopedia.com/ask/answers/121814/what-good-
            interest-coverage-ratio.asp
    """
    raise NotImplementedError("Interest coverage not implemented yet")


def eps_growth(current_year, prior_year):
    """
    EPS growth (earnings per share growth) illustrates the growth of earnings
    per share over time. EPS growth rates help investors identify stocks that
    are increasing or decreasing in profitability.

    Example:
        Fiscal Year  Basic EPS Incl Extra Items  Growth
        2017-09-30   2.32                        11.0%
        2018-09-29   3                           29.6%
        2019-09-28   2.99                        -0.4%
        2020-09-26   3.31                        10.6%
        2021-09-25   5.67                        71.3%

        Basic EPS Growth  = (Current Year - Prior Year) / ABS(
            Prior Year Basic EPS Incl Extra Items)*
        63.0% = ($6.07 M - $3.723 M) / $3.723 M

    Comment:
        The growth in EPS should be consistent. It's okay for the growth to
        fluctuate during hard times, as long as the general trend is upward.
        But if the EPS fluctuates one too many times, it's not worth it to
        attempt to value the company.

    Returns:
        TODO: Add returns
    """
    return (current_year - prior_year) / prior_year


def cash_flow_ratios(operating_cash_flow, current_liabities):
    """
    The operating cash flow ratio is calculated by dividing operating cash
    flow by current liabilities. Operating cash flow is the cash generated by
    a company's normal business operations.

    Example:
        TODO: Add example

    Comment:
         I don't look at all the Cash Flow Ratios, so much as understand how
         the Cash Flows happen. The basic requirement is, of course, a positive
         Cash Flow from Operations. It also helps to understand how the cash
         flows happen in the investing and financing side of the business.

    Returns:
        TODO: Add returns
    """
    return operating_cash_flow / current_liabities


def current_ratio(current_assets, current_liabilities):
    """
    Current Ratio measures whether a firm is capitalized with enough assets to
    pay its debts over the next twelve months by comparing a firm's current
    assets to its current liabilities.

    While ratios vary by industry and circumstances, healthy companies
    generally have ratios between 1.5 and 3.

    A high current ratio is not necessarily a good thing. The company may be
    inefficiently using its current assets or short-term financing facilities.

    While a low current ratio (values less than 1) may indicate that a firm is
    having difficulty meeting current obligations, it may also reflect the
    organizations ability to borrow against good prospects to meet current
    obligations. Strong businesses that can turn inventory faster than due
    dates on their accounts payable may also have a current ratio less than
    one.

    Example:
        Fiscal Year  Current Assets  Current Liabilities  Current Ratio
        2017-09-30   $128.6 B        $100.8 B             1.3x
        2018-09-29   $131.3 B        $115.9 B             1.1x
        2019-09-28   $162.8 B        $105.7 B             1.5x
        2020-09-26   $143.7 B        $105.4 B             1.4x
        2021-09-25   $134.8 B        $125.5 B             1.1x

        Current Ratio = Current Assets / Current Liabilities
        $153.2 B / 147.6 B = 1.0x

    Comment:
        A Current Ratio of at least 2 is present in good companies.
        The important thing would be to understand what constitutes
        Current Assets and Current Liabilities. A Current Ratio of 3 is
        of no use if Current Assets is made up of a lot of bad receivables
        or useless inventory. This is where looking at the
        Receivables/Payables/Inventory Ratios will come in handy.

    Returns:
        TODO: Add returns
    """
    return current_assets / current_liabilities


def r_and_d_total_investments(r_and_d, total_investments):
    """
    R&D: Research and development (R&D) include activities that companies
        undertake to innovate and introduce new products and services. It is
        often the first stage in the development process. The goal is typically
        to take new products and services to market and add to the company's
        bottom line.

    Investment: An investment is an asset or item acquired with the goal of
        generating incomeor appreciation. For example, an investor may
        purchase a monetary asset now with the idea that the asset will provide
        income in the future or will later be sold at a higher price for a
        profit.

    Example:
        TODO: Add example

    Comment:
        Once again, understand what constitutes Long Term Investments. If these
        are investments like Land, Building etc., which are likely to have a
        market value in excess of the book value, that would be useful.
        Raymond's Fixed Assets are almost 50% if its Total Assets. If you look
        at Raymond's Annual Reports, you will understand that these Assets
        are mostly Real Estate and Investments which are recorded at book
        value. but actually have fair values much above the book value.

    Returns:
        TODO: Add returns
    """
    return r_and_d / total_investments


def long_term_investments_total_investments():
    raise NotImplementedError(
        "Long term investments / total investments not implemented yet"
    )


def return_on_assets(net_income, average_total_assets):
    """
    The term return on assets (ROA) refers to a financial ratio that indicates
    how profitable a company is in relation to its total assets.

    Example:
        Fiscal Year  Net Income  Avg Assets  Return On Assets
        2017-09-30   $48.351 B   $348.5 B    13.9%
        2018-09-29   $59.531 B   $370.5 B    16.1%
        2019-09-28   $55.256 B   $352.1 B    15.7%
        2020-09-26   $57.411 B   $331.2 B    17.3%
        2021-09-25   $94.68 B    $337.4 B    28.1%

        ROA = Net Income / Average Total Assets
        $100.6 B / $367.6 B = 27.4%

    Comment:
        There is no optimum number, but a good RoA should compensate for a low
        Profit Margin (If that is indeed the case). Raymond has an Asset
        Turnover of 1.27, which is exceptionally good for a company its size.
        It's getting the most out of its Assets. This is why I continue to
        hold Raymond, regardless of the low Margin Ratios. RoA is more
        important for BFSI companies than it is for manufacturing companies,
        but the logic still holds the same.

    Returns:
        TODO: Add returns
    """
    return net_income / average_total_assets


def return_on_equity():
    raise NotImplementedError("Return on equity not implemented yet")


def growth_in_retained_earnings():
    raise NotImplementedError("Growth in retained earnings not implemented yet")


def profit_growth_and_sales_growth():
    raise NotImplementedError("Profit Growth and Sales Growth not implemented yet")


def profit_growth_to_sales_growth():
    raise NotImplementedError("Profit Growth-to-Sales Growth not implemented yet")


def peg_ratio(peg_ratio, eps_growth_rate):
    """
    PEG Ratio is a valuation metric for determining the relative trade-off
    between the price of a stock, the earnings per share (EPS), and the
    company's trailing EPS growth rate. A lower ratio is considered 'better'
    (cheaper) and a higher ratio is 'worse' (expensive).

    Example:
        Date         P/E Ratio   EPS Growth Rate  PEG Ratio
        2017-09-30   17.1        2.7              6.3
        2018-09-29   19.4        25.3             0.8
        2019-09-28   18.2        6.7              2.7
        2020-09-26   33.9        11.9             2.9
        2021-09-25   26.9        55.1             0.5

        PEG Ratio = PEG Ratio / Trailing EPS Growth Rate
        26.9 / 55.1 = 0.5

    Comment:
        Although I tend to shy away from companies with P/E greater than 40, I
        hardly ever look at the P/E otherwise. The PEG Ratio, which accounts
        for the growth in earnings (Which makes up a major part of the
        intrinsic value of a company) is a much more logical valuation ratio
        to look at. An under-valued company should have a PEG less than 1,
        but even a PEG of 1.5 is acceptable. If you are looking at a company
        having a Dividend Yield >1% or so, make sure to add its Dividend Yield
        as well to the denominator (EPS Growth + Dividend Yield).

    Returns:
        TODO: Add returns
    """
    return peg_ratio / eps_growth_rate
