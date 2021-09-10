goodCreditScore=True
goodSalary=False

if goodCreditScore and goodSalary:
    print("Your loan is approved")
else:
    if goodCreditScore or goodSalary:
        print("We will consider your application")
    else:
        print("Your loan is rejected!")