<<<<<<< HEAD
# Test-suite

This folder contains the PySoftK unit-test suite. It is written
to be used in combination with the pytest library, which is required and 
installed in the setup.py file. 

# How to run the test-suite?

To run the test-suite, you need to go to the test folder and type

pytest

Once this is done the following result should appear:

# Result of the tests:

============= test session starts ================

platform linux -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0

collected 18 items                                                                                               

test_chains_func.py .....       [ 27%]

test_folders_func.py ...        [ 44%]

test_format_print.py ....       [ 66%]

test_htp.py .....               [ 72%]

test_sm_func.py .....           [100%]


====================== 18 passed in 26.29s ========
=======
<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-76%25-yellow.svg" /></a><br/><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>/home/runner/.local/lib/python3.9/site-packages/pysoftk/folder_manager</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/folder_manager/folder_creator.py">folder_creator.py</a></td><td>51</td><td>3</td><td>94%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/folder_manager/folder_creator.py#L38">38</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/folder_manager/folder_creator.py#L153-L154">153&ndash;154</a></td></tr><tr><td colspan="5"><b>/home/runner/.local/lib/python3.9/site-packages/pysoftk/format_printers</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/format_printers/format_mol.py">format_mol.py</a></td><td>27</td><td>6</td><td>78%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/format_printers/format_mol.py#L49-L50">49&ndash;50</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/format_printers/format_mol.py#L72-L73">72&ndash;73</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/format_printers/format_mol.py#L95-L96">95&ndash;96</a></td></tr><tr><td colspan="5"><b>/home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py">calculator_htp.py</a></td><td>82</td><td>38</td><td>54%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py#L137-L162">137&ndash;162</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py#L181-L189">181&ndash;189</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py#L269-L275">269&ndash;275</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py#L338-L343">338&ndash;343</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/htp_tools/calculator_htp.py#L371-L383">371&ndash;383</a></td></tr><tr><td colspan="5"><b>/home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/calculators.py">calculators.py</a></td><td>41</td><td>41</td><td>0%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/calculators.py#L1-L140">1&ndash;140</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/linear_polymer.py">linear_polymer.py</a></td><td>80</td><td>3</td><td>96%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/linear_polymer.py#L194">194</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/linear_polymer.py#L250-L251">250&ndash;251</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/super_monomer.py">super_monomer.py</a></td><td>51</td><td>7</td><td>86%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/linear_polymer/super_monomer.py#L154-L162">154&ndash;162</a></td></tr><tr><td colspan="5"><b>/home/runner/.local/lib/python3.9/site-packages/pysoftk/torsional</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/torsional/torsional.py">torsional.py</a></td><td>88</td><td>10</td><td>89%</td><td><a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/torsional/torsional.py#L59-L60">59&ndash;60</a>, <a href="https://github.com/alejandrosantanabonilla/pysoftk/blob/main//home/runner/.local/lib/python3.9/site-packages/pysoftk/torsional/torsional.py#L238-L249">238&ndash;249</a></td></tr><tr><td><b>TOTAL</b></td><td><b>455</b></td><td><b>108</b></td><td><b>76%</b></td><td>&nbsp;</td></tr></tbody></table></details>

| Tests | Skipped | Failures | Errors | Time |
| ----- | ------- | -------- | -------- | ------------------ |
| 20 | 0 :zzz: | 0 :x: | 0 :fire: | 41.825s :stopwatch: |

<!-- Pytest Coverage Comment:End -->

# PySoftK


**PySoftK** is a set of Python tools and programs for modelling and simulating polymers with different topologies. The program is still under active 
development and contributions are welcome. A complete introduction into the program can be found in this link [Documentation][1]. To quickly install 
**PySoftk**, we encourage to do it inside a virtual environment, which can be achieved in the following way:

1. Create a directory named as you want and access it (in this case called work_pol):

```bash 
  [~] mkdir work_pol
  [~] cd work_pol
```

2. Create a virtual environment named pol (this name can be changed, of course) and activate the environment:

```bash 
   [~] python -m venv pol
   [~] source pol/bin/activate
```

3. Get PySoftK from the GitHub repository:

```bash 
  git clone https://github.com/alejandrosantanabonilla/pysoftk.git
```

4. Install PySoftK in this folder using the virtual environment

```bash 
   [~] cd pysoftk
   [~] pip install .
```

**NOTE:** To use the **calculators** option, the code [xtb][2] needs to be installed and linked to the executable using the command:

```bash  
   export PATH="$PATH:$HOME/PATH_TO_FOLDER/xtb-X.X.X/bin"
   export XTBHOME="PATH_TO_XTB_FOLDER/xtb-X.X.X"
   ulimit -s unlimited
```

Replacing **PATH_TO_FOLDER** by the actual path where xtb is stored in your computer.
  
5. For testing PySoftK, you need to go to the folder **test** and then type:

```bash 
  pytest
```

[1]: https://alejandrosantanabonilla.github.io/pysoftk/
[2]: https://github.com/grimme-lab/xtb
>>>>>>> c6f7409ba1533dd4f4a9e8f2f76c8a9666e2731f