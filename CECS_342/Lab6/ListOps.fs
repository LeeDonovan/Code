module ListOps
//Lab 6: Donovan Lee and Brian Tran 


type Account =
    | Balance of int
    | Overdrawn of int
    | Empty

type Customer = { Name: string; Account: Account }

let makeCustomerWithBalance name (amount: int) =
    let account =
        if amount > 0 then
            Balance amount
        elif amount < 0 then
            Overdrawn(abs amount)
        else
            Empty

    { Name = name; Account = account }

let unknownCustomer = makeCustomerWithBalance "Unknown" 0

let maxBalance name coll = 
  let getBalance coll =
    match coll with
    | Balance b -> true
    | _ -> false

  let onlyBalance  = coll |> List.filter(fun c -> c.Name = name && getBalance c.Account)
  
  
  let rec maxBalance' name coll acc = 
    match coll with// list is now filtered with only customers name and Account type Balance
    | [] -> acc //if list is empty return unknownCustomer
    | h :: t -> if acc.Account = Empty then
                                            maxBalance' name t h
                                          else
                                            if h.Account > acc.Account then
                                                maxBalance' name t h
                                            else
                                              maxBalance' name t acc


  maxBalance' name onlyBalance unknownCustomer
        //| coll |> List.filter(makeCustomerWithBalance c.Name amount -> if amount <= 0 then //unknownCustomer)

let totalOverdrawn name coll = 
  let getOverDrawn coll =
    match coll with 
    | Overdrawn od -> true
    | _ -> false
  
  let onlyOverdrawn = coll |> List.filter(fun c -> c.Name = name && getOverDrawn c.Account)
  
  
  let rec totalOverdrawn' name coll acc = 
    match coll with 
    |[] -> 0
    |h :: t when h.Name = name -> 
                                match h.Account with
                                | Overdrawn od -> od + totalOverdrawn' name t acc 
                                | _ -> 0
    | _::t -> totalOverdrawn' name t acc

  totalOverdrawn' name coll 0