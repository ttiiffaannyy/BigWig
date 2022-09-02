import random
random.seed(20220831)
name_lst = ['Miriam', 'Steve', 'Yang', 'Lior', 'Matt', 'Ben', 'Cecilia','Tzur', 
            'Linh','Fran C', 'Jenny', 'Nina', 'Tiffany', 'Lee', 'Kevin','Fran Z', 
            'Daniel', 'Eric']
name_list_shuffled = name_lst.copy()
# shuffle the new list
random.shuffle(name_list_shuffled)
name_list_shuffled 



class big_wig(object):
    
    def __init__(
        self,        
        name_lst = [],
        timezone_challenge = [],
        start_date = datetime(dxxxx)
        num_bigwigs = 3,
        
    ):
        """
        Big wig function -
        (1) can fit sub-daily, daily, weekly and monthly data.
        (2) for monthly data, holiday component will not be fitted; for weekly data, the holiday will be moved to the
        date in the history dataframe for which the effect is desired; for daily data, holiday will be naturally fitted
        (3) for sub-daily data, current calculation of daily seasonality does not distinguish weekday and weekend and
        assumes they are the same; also, holiday component will not be fitted (for now).
        :param data: dataframe. contains at least two columns: time column and target column.
        :param time_var: str.
        :param target: str.
        :param task: str.
        :param holidays: list.
        :param prefix: str.
        :param country_or_region: str.
        """

        self.name_lst = name_lst
        self.timezone_challenge = timezone_challenge
        self.num_bigwigs = num_bigwigs      

    def calc_shap(self):

        """
        (1) Check frequency of timestamp column in data by calculating the minimum time difference.
        Set time frequency to 'H', 'D', 'W', 'M' or raise exception.
        (2) infer time frequencies - e.g., 'M' for end of month and 'MS' for start of month, which will be used in
        creating future dataframe for forecasting.
        :return:
        """

        self.start = self.data[self.time_var].min()
        history_end = self.data[self.time_var].max()

        dt = self.data[self.time_var].diff()
        min_dt = dt.iloc[dt.values.nonzero()[0]].min()

        if min_dt < pd.Timedelta(days=1):
            self.freq = 'H'
            delta = timedelta(hours=int(self.horizon))
        elif min_dt == pd.Timedelta(days=1):
            self.freq = 'D'
            delta = timedel
        return xxxx
    
    def create_schedule(self):
        
        # link names to specific date (Monday of the week)
        
