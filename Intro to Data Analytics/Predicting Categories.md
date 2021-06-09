# Predicting Categories

## K-Means

### RapidMiner:

One `ReadCSV` operator for _training_ data.

Another `ReadCSV` operator for _testing_/_scoring_ data.

`LDA` (Linear Discriminant Analysis) operator

`k-NN` operator

`Naive Bayes` (basic) operator

Right click to enable/disable operators.

Set the id column's role to id.
All data types need to be numeric.

`Select Attributes` set _subset_, select all but non-numeric ones.

`Set Role` set the _dependent_ attribute to _label_.

Connect _Training_ to _Select Attributes_ to _Set Role_ to _LDA_ (or _k-NN_, _Naive Bayes_).

`Apply Model` operator to use a model.

Connect _LDA_ output and _Scoring_ output to _Apply Model_.
