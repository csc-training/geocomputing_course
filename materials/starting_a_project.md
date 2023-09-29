# First steps for fast jobs 

- Spend a little time to investigate:
   - Which of the available software would be the best to solve the kind of problem you have?
      - Ask experienced colleagues or <servicedesk@csc.fi> for guidance
- Consider:
   - The software that solves your problem fastest might not always be the best
      - Issues like ease-of-use and compute power/memory/disk demands are also highly relevant
   - Quite often it is useful to start simple and gradually use more complex approaches if needed
- When you've found the software you want to use, check if it is available at CSC as a [pre-installed optimized version](https://docs.csc.fi/apps/)
   - Familiarize yourself with the software manual, if available
- If you need to install a software package distributed through Conda, [you need to containerize it](https://docs.csc.fi/computing/usage-policy/#conda-installations)
   - Containerizing greatly speeds up performance at startup and can be done easily with the [Tykky wrapper](https://docs.csc.fi/computing/containers/tykky/)
- If you can't find suitable software, consider writing your own code