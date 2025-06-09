
class emp(object):
    def __init__(self,name,age,salary,domain):
        self.name=name
        self.age=age
        self.salary=salary
        self.domain=domain

class fresher_emp(emp):
    def __init__(self,name,age,salary,domain,emp_id):
        emp.__init__(self,name,age,salary,domain)
        self.id = emp_id


class exp_emp(emp):
    def __init__(self, name, age, salary, domain, years_of_ex, pf_no, com_name):
        emp.__init__(self,name,age,salary,domain)
        self.yoe = years_of_ex
        self.pfno = pf_no
        self.cname = com_name






suresh : fresher_emp = fresher_emp('suresh',23,50000,'Python developer',1234)

reddypasand : exp_emp = exp_emp('reddy prasnad',21,45000,'devops','5+',120320420,'L&T')




