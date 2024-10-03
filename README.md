# 113-1-NTU-Fintech-Code
This file is a record of the NTU Fintech course during the 113-1 semester.

## HW1
### Function prototype
   ```bash
   irr=irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod)
   ```
- ```irr```: Internal rate of return
- ```cashFlowVec```: vector of cash flow
- ```cashFlowPeriod```: An integer of period (in month) for cash flow
- ```compoundPeriod```: An integer of period (in month) for compounding, which should be a factor of cashFlowPeriod. (For instance, if cashFlowPeriod=12, compoundPeriod could be 1, 2, 3, 4, 6, 12.)

### Usage examples
- ```irrFind(cashFlowVec, 12, 12)```: Yearly payment/collection, yearly compounding
- ```irrFind(cashFlowVec, 12, 3)```: Yearly payment/collection, quarterly compounding
- ```irrFind(cashFlowVec, 12, 1)```: Yearly payment/collection, monthly compounding
- ```irrFind(cashFlowVec, 3, 1)```: quarterly payment/collection, monthly compounding

### Numerical examples
- ```irrFind([-1234,362,548,481], 12, 12)``` returns 0.059616
- ```irrFind([-1234,362,548,481], 12, 1)```: returns 0.058047
- ```irrFind([-16320,-16157,-16157,-16157,-16157,-16157,100000], 12, 12)``` returns 0.008389
- ```irrFind([-59356,-58762,-58762,-58762,-58762,-58762,380000], 12, 1)``` returns 0.020738
