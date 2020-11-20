#-------------------------------------------------------------------------------
#    Combine Two Tables
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/combine-two-tables/
# Completed 11/18/20
#-------------------------------------------------------------------------------

"""
1. Left join
"""

SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person P LEFT JOIN Address A
ON P.PersonId = A.PersonId