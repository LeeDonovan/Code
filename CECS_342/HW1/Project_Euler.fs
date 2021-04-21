open System

let isPrime n = 
  let mutable nums = []
  let mutable check = true
  for i in 2 .. n-1 do
    if n % i = 0 then
      nums <- [i] |> List.append nums
    if nums.IsEmpty then
      check <- true
    else
      check <- false
  //printfn "List: %A" nums
  check

let sumPrimes max = 
  let mutable sum = 0
  let mutable i = 3
  while i <= max do
    let mutable check = isPrime i
    if check then
      sum <- sum + i 
      i <- i + 1
    else
      i <- i + 1
  sum <- sum + 2
  sum

[<EntryPoint>]
let main args =
  printfn "Enter a number to check if it is prime:  "
  let num = int32 (Console.ReadLine())
  let mutable check_prime = isPrime num
  if check_prime then
    printfn "%d is a prime number!" num
  else
    printfn "%d is not a prime number!" num
  let mutable summation = sumPrimes num
  printfn "The sum of primes for %d is %d" num summation
  0