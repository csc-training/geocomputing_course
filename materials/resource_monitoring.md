# CSC project resource monitoring

## my.csc.fi

* Manage your account
* Manage your projects/services
* Estimate billing units
* Change password
* ...

[`https://my.csc.fi`](https://my.csc.fi)

## Billing units

- CPU time and storing files consume "[Billing units](https://docs.csc.fi/accounts/billing/)" (BU)
- BUs are a property of computing projects not users
- Monitor the BU usage with command `csc-projects` in the command line
   - For help/options, try `csc-projects -h`
- Batch job billing scheme:
   - Amount of resources allocated: All requested resources are billed ie. number of cores, amount of memory
   - Time allocated: Resources are billed based on the actual (wall) _time_ a job has **used**, not the reserved maximum time

### Applying for billing units

- Billing units can be also applied via [My Projects page in MyCSC](https://my.csc.fi/welcome)
   - Please [acknowledge using CSC](https://docs.csc.fi/support/faq/how-to-cite-csc/) resources in your publications
   - Please also inform us about your work by adding your publications to the resource application!
- Academic usage is one of the [free-of-use cases](https://research.csc.fi/pricing)
- You can estimate [usage with the online billing calculator](https://research.csc.fi/billing-and-monitoring#buc) 
   - The calculator can also be used to estimate the value of the resources



