def read_log_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def count_user_activity(log_generator):
    user_counts = {}
    for entry in log_generator:
        parts = entry.split(' - ')
        if len(parts) == 2:
            user = parts[1].split()[0]
            user_counts[user] = user_counts.get(user, 0) + 1
    return user_counts


if __name__== "__main__":
    log_generator = read_log_file("user_activity.txt")
    user_activity_counts = count_user_activity(log_generator)
    print(user_activity_counts)