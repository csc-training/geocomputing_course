# CSC accounts and projects

To access any of CSC computing and many of the storage services, a **CSC account** is needed. 

Every CSC account must be linked with a **CSC project**, which enables you to share resources and data among your group. A project needs a project manager, who creates the project, manages the user accounts and services that belong to the project and is responsible of the resource usage. The project manager is typically a leader of a research team or other senior researcher. 

CSC services are **free of charge** for open science at Finnish higher education institutions and research institutes.

[CSC Docs: Accounts and projects](https://docs.csc.fi/accounts/)

:::{admonition} Course project
:class: hint

You can now also create so called `course project` for use in education.

Note: 
* Course projects are valid for maximum 6 months
* Projects cannot be extended
* Project data will be deleted when the project has ended

[CSC Docs: Course project](https://docs.csc.fi/accounts/how-to-create-new-project/#how-to-create-a-course-project)
:::




## Managing resources

Your first steps into many CSC services goes via [`https://my.csc.fi`](https://my.csc.fi):

* Create an account
* Manage your account
   * Keep it alive by password update once a year
* Manage your projects/services
* Estimate billing units
* Change password
* ...


## Billing units

- CPU time and storing files consume "Billing units" (BU)
- BUs are a property of computing projects not users
- Monitor the BU usage with command `csc-projects` in the command line
   - For help/options, try `csc-projects -h`
- Batch job billing scheme:
   - Amount of resources allocated: All requested resources are billed ie. number of cores, amount of memory
   - Time allocated: Resources are billed based on the actual (wall) _time_ a job has **used**, not the reserved maximum time

[CSC Docs: Billing units](https://docs.csc.fi/accounts/billing/)

### Applying for billing units

- Billing units can be also applied via [My Projects page in MyCSC](https://my.csc.fi/welcome)
   - Please acknowledge use of CSC resources in your publications ([CSC Docs: CSC Acknowledgement](https://docs.csc.fi/support/faq/how-to-cite-csc/)); many tools pages also provide a copyable acknowledgement examples (see for example [CSC Docs: QGIS acknowledgement](https://docs.csc.fi/apps/qgis/#acknowledgement))
   - Please also inform us about your work by adding your publications to the resource application!
- Academic usage is one of the [free-of-use cases](https://research.csc.fi/pricing)
- You can estimate [usage with the online billing calculator](https://research.csc.fi/billing-and-monitoring#buc) 
   - The calculator can also be used to estimate the value of the resources



