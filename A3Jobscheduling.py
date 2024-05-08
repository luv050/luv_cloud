
profit = []
jobs = []
deadline = []

n = int(input("Enter the number of jobs: "))

for i in range(n):
    p = int(input("Enter the profit of job {}: ".format(i+1)))
    profit.append(p)
    j = input("Enter the name of job {}: ".format(i+1))
    jobs.append(j)
    d = int(input("Enter the deadline of job {}: ".format(i+1)))
    deadline.append(d)
    
profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

slot = [0] * (n+1)
profit = 0
ans = ['null'] * (n+1)

for i in range(n):
    job = profitNJobs[i]
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break
print("Jobs scheduled:", ans[1:])
print("Total profit:", profit)
