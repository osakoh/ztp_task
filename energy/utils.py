def rate_details(rate_name):
    """:returns the rate price(£/Kwh) for a rate name """
    switch = {
        "day_rate": 0.0732,
        "night_rate": 0.055,
        "weekend_rate": 0.063,
        "weekend_day_rate": 0.067,
        "weekend_night_rate": 0.063,
    }
    return switch.get(rate_name, 0)


def process(rate_name):
    """
    replaces a space with and underscore then converts to lower case.
    Ex:
        input: Weekend Night Rate
        output: weekend_night_rate
    """
    return rate_name.replace(" ", "_").lower()


def excel(wb, pd_ref):
    """
    wb: takes an excel workbook as input
    pd_ref: reference to Pandas library
    returns: the customer's details in a single list and ratings in a multidimensional list
    """
    # process workbook
    xls = pd_ref.ExcelFile(wb)
    # get all sheet names
    sheet_names = xls.sheet_names
    # ['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4']
    sheet_names = sheet_names[0:4]

    # Customer details only for one sheet
    df = pd_ref.read_excel(xls, sheet_name="Customer 1", header=0)
    # extract customer name, address, and meter number
    cus_df = df.iloc[0:2, 1:2]
    # convert to list - ['Noel', '2, Covent Garden, London', 'YYYYYYYY']
    cus_list = cus_df.columns.values.tolist() + cus_df.values.flatten().tolist()

    # Customer ratings only for one sheet
    rating_df = df.iloc[4:, 0:3]
    # convert to list - [['Day Rate', 1000, 1600], ['Night Rate', 2245, 2350], ['Weekend Rate', 2850, 3200]]
    rating_list = rating_df.values.tolist()

    # read all sheets and extract first 5 rows, 3 columns
    # for sheet in sheet_names:
    #     print('##################################  ' + tab + '   ##################################')
    #     df = pd.read_excel(xls, sheet, header=0)
    #     print(df.iloc[0:2, 1:2])

    return [cus_list, rating_list]


"""
# process workbook
            xls = pd.ExcelFile(workbook)
            # get all sheet names
            sheet_names = xls.sheet_names
            # ['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4']
            sheet_names = sheet_names[0:4]

            # Customer details only for one sheet
            df = pd.read_excel(xls, sheet_name="Customer 3", header=0)
            # extract customer name, address, and meter number
            cus_df = df.iloc[0:2, 1:2]
            # convert to list - ['Noel', '2, Covent Garden, London', 'YYYYYYYY']
            cus_list = cus_df.columns.values.tolist() + cus_df.values.flatten().tolist()

            # Customer ratings only for one sheet
            rating_df = df.iloc[4:, 0:3]
            # convert to list - [['Day Rate', 1000, 1600], ['Night Rate', 2245, 2350], ['Weekend Rate', 2850, 3200]]
            rating_list = rating_df.values.tolist()

"""
