from ukuni_rankings import rankings, overall_rankings
import csv

math_rks = rankings("mathematics")
cs_rks = rankings("computer-science")
ovrl_rks = overall_rankings()
with open("ukuni_rankings.csv", mode="w", newline="") as uni_rks:
    uni_writer = csv.writer(uni_rks)
    uni_writer.writerow(
        ["University Name", "Overall Rank", "Mathematics Rank", "Computer Science Rank"]
    )
    for row in ovrl_rks:
        uni = row[0]
        ovrl_rk = row[1]
        math_rk = "N/A"
        cs_rk = "N/A"
        if uni in math_rks:
            math_rk = math_rks[uni]
        if uni in cs_rks:
            cs_rk = cs_rks[uni]
        uni_writer.writerow([uni, ovrl_rk, math_rk, cs_rk])
