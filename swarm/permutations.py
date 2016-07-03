# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Template file used by ExpGenerator to generate the actual
permutations.py file by replacing $XXXXXXXX tokens with desired values.

This permutations.py file was generated by:
'C:\Python27\lib\site-packages\nupic\swarming\exp_generator\ExpGenerator.pyc'
"""

import os

from nupic.swarming.permutationhelpers import *

# The name of the field being predicted.  Any allowed permutation MUST contain
# the prediction field.
# (generated from PREDICTION_FIELD)
predictedField = 'DayTotal'




permutations = {
  'aggregationInfo': {   'days': 0,
    'fields': [],
    'hours': 0,
    'microseconds': 0,
    'milliseconds': 0,
    'minutes': 0,
    'months': 0,
    'seconds': 0,
    'weeks': 0,
    'years': 0},

  'modelParams': {
    

    'sensorParams': {
      'encoders': {
          u'DayTotal': PermuteEncoder(maxval=230, fieldName='DayTotal', w=21, clipInput=True, minval=0, encoderClass='ScalarEncoder', n=PermuteInt(22, 521), ),
  '_classifierInput': dict(maxval=230, classifierOnly=True, clipInput=True, minval=0, n=PermuteInt(28, 521), fieldname='DayTotal', w=21, type='ScalarEncoder', ),
  u'Date_timeOfDay': PermuteEncoder(fieldName='Date', encoderClass='DateEncoder.timeOfDay', radius=PermuteFloat(0.5, 12), w=21, ),
  u'Date_dayOfWeek': PermuteEncoder(encoderClass='DateEncoder.dayOfWeek', radius=PermuteFloat(1, 6), w=21, fieldName='Date', ),
  u'Date_weekend': PermuteEncoder(encoderClass='DateEncoder.weekend', radius=PermuteChoices([1]),  w=21, fieldName='Date', ),
      },
    },

    'spParams': {
        'synPermInactiveDec': PermuteFloat(0.0003, 0.1),

    },

    'tpParams': {
        'activationThreshold': PermuteInt(12, 16),
  'minThreshold': PermuteInt(9, 12),
  'pamLength': PermuteInt(1, 5),

    },

    'clParams': {
        'alpha': PermuteFloat(0.0001, 0.1),

    },
  }
}


# Fields selected for final hypersearch report;
# NOTE: These values are used as regular expressions by RunPermutations.py's
#       report generator
# (fieldname values generated from PERM_PREDICTED_FIELD_NAME)
report = [
          '.*DayTotal.*',
         ]

# Permutation optimization setting: either minimize or maximize metric
# used by RunPermutations.
# NOTE: The value is used as a regular expressions by RunPermutations.py's
#       report generator
# (generated from minimize = "multiStepBestPredictions:multiStep:errorMetric='altMAPE':steps=\[1\]:window=1000:field=DayTotal")
minimize = "multiStepBestPredictions:multiStep:errorMetric='altMAPE':steps=\[1\]:window=1000:field=DayTotal"

minParticlesPerSwarm = 3

inputPredictedField = 'yes'







maxModels = 1



def permutationFilter(perm):
  """ This function can be used to selectively filter out specific permutation
  combinations. It is called by RunPermutations for every possible permutation
  of the variables in the permutations dict. It should return True for valid a
  combination of permutation values and False for an invalid one.

  Parameters:
  ---------------------------------------------------------
  perm: dict of one possible combination of name:value
        pairs chosen from permutations.
  """

  # An example of how to use this
  #if perm['__consumption_encoder']['maxval'] > 300:
  #  return False;
  #
  return True
