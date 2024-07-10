import re
from functools import cmp_to_key


def sort_ips(ips: list):
    length = len(ips)
    if length <= 1:
        return

    def compare_items(a: str, b: str):
        four_parts0 = a.split(sep=".")
        four_parts1 = b.split(sep=".")
        for i in range(0, 4):
            temp0 = int(four_parts0[i])
            temp1 = int(four_parts1[i])
            if temp0 < temp1:
                return -1
            elif temp0 > temp1:
                return 1
            else:
                continue
        return 0

    ips.sort(key=cmp_to_key(compare_items))


def recognize_and_sort_IPs(path_str):
    ips = []
    with open(path_str, "r") as f:
        text = f.read()
        lines = text.split(sep="\n")
        # ip_and_http_pattern = re.compile(
        #     # r"^(\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3}) - - \[.*\] \".+\" (\d+) \d+ \".+\" \".+\""
        #     r"^(\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3}).+"
        # )
        ip_and_status_pattern = re.compile(
            r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.*\] \"[A-Z]+ .*\" 200"
        )
        for line in lines:
            match = ip_and_status_pattern.search(line)
            if match:
                ips.append(match.group(1))
    sort_ips(ips)
    print(ips)


if __name__ == "__main__":
    recognize_and_sort_IPs("nginx.log")
