pool_volume_in_lt = int(input())
flow_rate_first_pipe_per_hour = int(input())
flow_rate_second_pipe_per_hour = int(input())
hours_worker_away = float(input())

first_pipe_flow = flow_rate_first_pipe_per_hour * hours_worker_away
second_pipe_flow = flow_rate_second_pipe_per_hour * hours_worker_away
total_pipe_flow = first_pipe_flow + second_pipe_flow

total_pipe_flow_in_perc = (total_pipe_flow / pool_volume_in_lt) * 100

first_pipe_flow_in_perc = (first_pipe_flow / total_pipe_flow) * 100
second_pipe_flow_in_perc = (second_pipe_flow / total_pipe_flow) * 100

diff = abs(pool_volume_in_lt - total_pipe_flow)

if total_pipe_flow <= pool_volume_in_lt:
    print(f"The pool is {total_pipe_flow_in_perc:.2f}% full.\
     Pipe 1: {first_pipe_flow_in_perc:.2f}%. Pipe 2: {second_pipe_flow_in_perc:.2f}%.")
else:
    print(f"For {hours_worker_away:.2f} hours the pool overflows with {diff:.2f} liters.")



