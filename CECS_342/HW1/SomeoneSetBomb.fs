open System

let placeTarget () = 
  let mutable y = Random().NextDouble()
  let mutable total = float(1000) * y
  let mutable round = 0.0
  round <- Math.Round(total, 2)
  round

let getAngle () = 
    let mutable keep_going = true
    printfn "Enter an angle to fire the cannon at: "
    let mutable input = float (Console.ReadLine())
    
    while keep_going do 
      if input < 0.0 || input > 90.1 then
        printfn "Can not shoot at that angle please try again: "
        input <- float (Console.ReadLine())
      else
        keep_going <- false
    input <- input * Math.PI/180.0
    input

let getGunpowder () = 
  let mutable keep_going = true
  printfn "Give a positive amount of gunpowder to use: "
  let mutable powder = float (Console.ReadLine())
  while keep_going do 
    if powder <= 0.0 then
        printfn "Give a positive amount of gunpowder, please try again: "
        powder <- float (Console.ReadLine())
    else
        keep_going <- false
  powder <- powder *30.0
  powder

let calculateDistance angle powder =
  let gravity = 9.81
  let velocity_y = powder * Math.Sin(angle)
  let velocity_x = powder * Math.Cos(angle)
  let apex = velocity_y/gravity
  let final_time = apex*2.0
  let final_distance = velocity_x * final_time
  final_distance
  
let isHit target distance = 
  if abs(target - distance) <= 1.0 then
    true
  else
    false


[<EntryPoint>]
let main args =
  let mutable keep_going = true
  let mutable targetRange = placeTarget()
  printfn "The target range is : %f meters away" (targetRange)
  while keep_going do
    let mutable angle = getAngle()
    let mutable range = getGunpowder()
    let mutable x_distance = float(calculateDistance angle range)
    let mutable marker = isHit targetRange x_distance
    let mutable t_dist = targetRange - x_distance
    if marker = true then
      keep_going <- false
      printfn "That's  a good hit"
    else
      if t_dist > 0.0 then
        printfn "Your shot landed %f short from the target" (t_dist)
      else
        printfn "Your shot landed %f long from the target" (t_dist * -1.0)
  // Return 0. This indicates success.
  0