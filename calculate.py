import math

goal_duration = 5
expected_rate_pa = 0.15
goal_size = 1500000

def showAmountToInvest(goal_duration,expected_rate_pa,goal_size):
	expected_rate_monthly = (1+expected_rate_pa)**(1/12)-1
	yearly_required = goal_size/((1+expected_rate_pa)**goal_duration)
	yearly_required_for_SIP = goal_size * expected_rate_pa / (1 + expected_rate_pa)/((1+ expected_rate_pa)**goal_duration - 1)
	monthly_required_for_SIP = goal_size * expected_rate_monthly / (1 + expected_rate_monthly)/((1+ expected_rate_monthly)**(goal_duration*12) - 1)

	print("ONE TIME INVESTMENT WITH EXPECTED GROWTH")
	print("Lump Some investment:{}".format(round(yearly_required)))
	#print("Monthly_investment: {}".format(round(yearly_required/12)))

	print("ANNUAL SIP WITH EXPECTED GROWTH")
	print("Yearly_investment:  {}".format(round(yearly_required_for_SIP)))
	print("Total investment:   {}".format(round(yearly_required_for_SIP*goal_duration)))
	print("Monthly_investment: {}".format(round(monthly_required_for_SIP)))
	print("Total investment:   {}".format(round(monthly_required_for_SIP*goal_duration*12)))

while(1):
	d = int(input("\nEnter total money you want at the end:"))
	r = int(input("Return pa in percent which your MF will give:"))/100
	t = int(input("how much time you will keep your money in MF:"))
	showAmountToInvest(t,r,d)


