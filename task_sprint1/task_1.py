text_time = "1h 45m,360s,25m,30m 120s,2h 60s"

total_minuts = 0

time_fragments = text_time.split(",")

for fragment in time_fragments:
    elements = fragment.split()

    for element in elements:
        if "h" in element:
            total_minuts += int(element.replace("h", "")) * 60
        if "m" in element:
            total_minuts += int(element.replace("m", ""))
        if "s" in element:
            total_minuts += int(element.replace("s", "")) // 60

print(total_minuts)
