# Manual

* `source/main.py`中最上面有`user config`，可自行設定
	* `dataset = 2` : 要使用哪個Data Set (有`1`, `2`可選擇)
	* `neuron = 2` : 幾個神經元(有`2`, `4`可選擇)
	* `times = 100` : 需要測試的次數，預設為`100`
	* `lr = 1.0` : learning rate
	* `output = open(str(neuron)+'neuron.out', "w")` : 輸出檔案位置

> 以上有限定範圍的變數請不要超出，我懶我沒做例外處理 感恩~