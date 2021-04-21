//Lab Partners -> Donovan Lee & Brian Tran

module ListOps

let suffixes coll =
  let rec suffixes' coll acc = 
    match coll with
    | [] -> []::acc
    | h :: t -> suffixes' t (coll :: acc)
    
  suffixes' coll [] |> List.rev
