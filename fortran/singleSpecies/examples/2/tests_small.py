#!/usr/bin/env python

# This python script checks the sfincsOutput.h5 file for an example to 
# see if the results are close to expected values.  This script may be
# run directly, and it is also called when "make test" is run from the
# main SFINCS directory.

execfile('../testsCommon.py')

desiredTolerance = 0.001

numFailures = 0

numFailures += shouldBe("transportMatrix", 0, -0.000630586, desiredTolerance)
numFailures += shouldBe("transportMatrix", 1, -0.00199776, desiredTolerance)
numFailures += shouldBe("transportMatrix", 2, -0.0620745, desiredTolerance)
numFailures += shouldBe("transportMatrix", 3,  -0.00199966, desiredTolerance)
numFailures += shouldBe("transportMatrix", 4, -0.0107542, desiredTolerance)
numFailures += shouldBe("transportMatrix", 5, -0.171768, desiredTolerance)
numFailures += shouldBe("transportMatrix", 6, -0.0621547, desiredTolerance)
numFailures += shouldBe("transportMatrix", 7, -0.172102, desiredTolerance)
numFailures += shouldBe("transportMatrix", 8, 35.0602, desiredTolerance)

exit(numFailures > 0)
