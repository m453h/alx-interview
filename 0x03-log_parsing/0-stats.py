#!/usr/bin/python3

"""
This script reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

It prints the statistics of total lines read after reading 10 lines or keyboard
interruption )CTRL + C)

Output format:
    -Total file size: File size: <total size>
     where <total size>  is the sum of all previous <file size>

    - Number of lines by status code:
    - Possible status code:
         - 200, 301, 400, 401, 403, 404, 405, 500

    - Prints nothing if the status code doesnt appear
      else prints in the format: <status code>: <number>

    - Status codes are printed in ascending order
"""
import sys


class LogParser:
    def __init__(self):
        """
        Initializes a new Instance of LogParser class
        """
        self.status_codes = ['200', '301', '400', '401',
                             '403', '404', '405', '500']
        self.total_size = 0
        self.stats = {}

    def display_stats(self):
        """
           Displays summary of the stats read from stdin.
        """
        print("File size: {}".format(self.total_size))
        for key in sorted(self.stats):
            print("{}: {}".format(key, self.stats[key]))

    def parse_line(self, line):
        """
        Parses input line
        line (string): The input line of log stream
        Returns (dict): Dictionary with size of line,
                        status code and
                        validity of read status code
        """
        line_parts = line.split()
        try:
            if line_parts[-2] in self.status_codes:
                is_valid_code = True
            else:
                is_valid_code = False

            return {
                "line_size": int(line_parts[-1]),
                "status_code": line_parts[-2],
                "is_valid_code": is_valid_code
            }
        except (IndexError, ValueError):
            return None

    def read_from_stdin(self):
        """
        Reads from standard input and displays stats
        after 10 lines or user interruption

        Raises:
            KeyboardInterrupt: If user presses (CTRL + C)
        """
        line_count = 0
        try:
            for line in sys.stdin:
                line_count += 1
                parsed_data = self.parse_line(line)

                if parsed_data is not None:
                    self.total_size += parsed_data["line_size"]
                    if parsed_data["is_valid_code"]:
                        if self.stats.get(parsed_data["status_code"]) is None:
                            self.stats[parsed_data["status_code"]] = 1
                        else:
                            self.stats[parsed_data["status_code"]] += 1
                if line_count % 10 == 0:
                    self.display_stats()
            self.display_stats()
        except KeyboardInterrupt:
            self.display_stats()


if __name__ == "__main__":
    parser = LogParser()
    parser.read_from_stdin()
