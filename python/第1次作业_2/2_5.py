total_minute=int(input())

minute=total_minute%60
total_hours=total_minute//60
hours=total_hours%24
total_days=total_hours//24
days=total_days%365
years=total_days//365

print('{}年{}天{}小时{}分钟'.format(years,days,hours,minute))
