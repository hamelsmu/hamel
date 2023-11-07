## Reveal Presentation

    library(tidyverse)
    library(palmerpenguins)
    1penguins |>
    2  mutate(
        bill_ratio = bill_depth_mm / bill_length_mm,
        bill_area  = bill_depth_mm * bill_length_mm
      )

1  
<span code-cell="annotated-cell-1" code-lines="3"
code-annotation="1">Take `penguins`, and then,</span>

2  
<span code-cell="annotated-cell-1" code-lines="4,5,6,7"
code-annotation="2">add new columns for the bill ratio and bill
area.</span>
