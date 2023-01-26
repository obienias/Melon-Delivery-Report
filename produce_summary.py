def melon_report(day, filepath):
    print (day)
    the_file = open(filepath)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()
    
melon_report("Day 1", "um-deliveries-day-1.txt")

melon_report("Day 2", "um-deliveries-day-3.txt")

melon_report("Day 3", "um-deliveries-day-3.txt")


