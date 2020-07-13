// question from: https://dev.to/thepracticaldev/daily-challenge-268-swapping-characters-in-strings-4n1g
function test(s, t) {
  // there's likely a better way
  let sArr = s.split('')
  let correctlyPlaced = new Array(sArr.length).fill(false)
  let moves = 0
  let i = 0
  while (i < sArr.length) {
    if (sArr[i] !== t[i]) { // found a dissimilar character
      let j = 0
      for (; j < i && !(sArr[i] === t[j] && !correctlyPlaced[j]); j++); // search the previous characters if there is one that will match and is misplaced
      if (j < i) {
        for (let k = i; k > j; k--) {
          [sArr[k], sArr[k - 1]] = [sArr[k - 1], sArr[k]] // do swaps
          correctlyPlaced[k] = false // mark everything else as miscorrectly placed for now
        }
        correctlyPlaced[j] = true // mark the index of the matching character to be correctly placed now
        moves += i - j
        i = j + 1
      } else {
        i++
      }
    } else {
      correctlyPlaced[i] = true
      i++
    }
  }

  // console.log(sArr, t)

  if (sArr.join('') !== t) return -1
  // console.log(moves)
  return moves
}

// console.log(test('sdeaf', 'sefda'))

console.log(test('abcd', 'acbd') === 1)
console.log(test('ab', 'ab') == 0)
console.log(test('ab', 'ba') == 1)
console.log(test('aaa', 'aaa') === 0)
console.log(test('sdeaf', 'sefda') === 3) // character a ahead of e needs to be moved to the right
console.log(test('sadbecf', 'sedbcaf') === 6)
console.log(test('sadasdcxs', 'sadasdacds') === -1) // character in s not in t
console.log(test('sadasdcss', 'sadasdacxs') === -1) // character in t not in s
