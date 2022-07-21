import os
import pandas as pd



class DataReader:
    def __init__(self, file_path) -> None:
        self.filepath = file_path

    def get_uid(self, filename, row_num):

        return f"{filename}_{row_num}"

    def read_file(self, path: str) -> list:
        """Read a file from path and returns list of the lines in the file

        Parameters
        ----------
        path : str
            file location path
        
        Returns:
        list
            the file content in a list
        """
        with open(path, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda l: l.strip('\n'), lines))
            return lines

    def parse(self, lines: list, filename: str) -> pd.DataFrame:
        """parses the lines into 5 columns and returns a pandas DataFrame

        Parameters
        ----------
        lines : list
            a list of lines from the source file
        filename : str
            the filename, used for generating unique identifiers

        Returns
        -------
        pd.DataFrame
            A dataframe holding all the lines
        """
        
        rows = {
        "uid": [],
        "track_id": [],
        "type": [],
        "traveled_distance": [],
        "avg_speed": [],
        "lat": [],
        "lon": [],
        "speed": [],
        "lon_acc": [],
        "lat_acc": [],
        "time": [],
        }
        for row_num, line in enumerate(lines):
            uid = self.get_uid(filename, row_num)
            line = line.split("; ")[:-1]
            # assert len(line[4:]) % 6 == 0, f"row number {row_num} caused the error: len(line[4:]) % 6 = {len(line[4:]) % 6}"
            assert len(line[4:]) % 6 == 0, f"{line}"
            track_id = int(line[0])
            veh_type = line[1]
            traveled_distance = float(line[2])
            avg_speed = float(line[3])
            for i in range(0, len(line[4:]), 6):
                rows["uid"].append(uid)
                rows["track_id"].append(track_id)
                rows["type"].append(veh_type)
                rows["traveled_distance"].append(traveled_distance)
                rows["avg_speed"].append(avg_speed)
                rows["lat"].append(float(line[4+i+0]))
                rows["lon"].append(float(line[4+i+1]))
                rows["speed"].append(float(line[4+i+2]))
                rows["lon_acc"].append(float(line[4+i+3]))
                rows["lat_acc"].append(float(line[4+i+4]))
                rows["time"].append(float(line[4+i+5]))
        
        df = pd.DataFrame(rows).reset_index(drop=True)
        return df


    def get_df(self, file_path: str=None, v=0) -> pd.DataFrame:
        """This calls the above two function. It takes the files path
        and returns a pandas dataframe object

        Parameters
        ----------
        file_path : str
            raw csv file path
        v: int
            verbosity selector

        Returns
        -------
        pd.DataFrame
            transformed version of csv as a pd.DataFrame
        """
        if not file_path and self.filepath:
            file_path = self.filepath

        lines = self.read_file(file_path)
        filename = file_path.split("/")[-1].strip(".csv")
        df = self.parse(lines, filename)
        if v>0:
            print(df.head())
            print(df.info())
        return df


if __name__ == "__main__":
    DataReader(file_path="../data/20181030_d1_0830_0900.csv").get_df(v=1)
