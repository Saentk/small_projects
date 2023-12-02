// task 1
console.log('\nTask 1')

arr = [1, 7, 5, 7, 4, 5, 5]

function fitsTheCondition(arr){
	result_arr = []
	for (let x = 0; x < (arr.length - 2); x++){
		result_arr.push(((arr[x] < arr[x+1]) & (arr[x+1] > arr[x+2]) 
	                  || (arr[x] > arr[x+1]) & (arr[x+1] < arr[x+2])))
	}
	return result_arr
}

console.log(fitsTheCondition(arr))



// task 2

console.log('\nTask 2')

matrix = [
	[4, 5, 6, 1, 2, 3],
	[1, 2, 3, 4, 5, 6],
	[9, 8, 7, 7, 8, 9]
];

function isRange(matrix){
	resultArray = []
	for (let x = 0; x < (matrix[1].length - 2); x++){
		arrToCheck = []
		for (let y = 0; y < 3; y++){
			arrToCheck.push(matrix[y][x], 
				matrix[y][x+1], matrix[y][x+2])
		}
		resultArray.push(JSON.stringify(arrToCheck.sort())
						==JSON.stringify([1,2,3,4,5,6,7,8,9]))
	}
	return resultArray
}

console.log(isRange(matrix))



// task 3

console.log('\nTask 3')

strings = [
['Hello', 'world'],
['Brad', 'came', 'to', 'dinner', 'with', 'us'],
['He', 'loves', 'tacos']
]

position = ['left', 'right', 'left']

// To change left - right position
function moveTo(str){
	if (pos == 'left') {str += ' '.repeat(16 - str.length)}
	else if (pos == 'right') {str = ' '.repeat(16 - str.length) + str}
	return str
}

function add_strings(str, row){
	for (let word = 0; word < str[row].length; word++){
		if ((string + str[row][word]).length <= 15){
			string += str[row][word] + ' '}
		else{
			text += '*' + moveTo(string.trim()) + '*' + '\n'
			string = str[row][word] + ' '}
	}
	return text += '*' + moveTo(string.trim()) + '*' + '\n'
}

function format_text(str, position){
	text = '******************\n'
	for (let row = 0; row < str.length; row++){
		string = ''
		pos = position[row]
		text = add_strings(str, row)
	}
	return text + '******************'
}

console.log(format_text(strings, position))



