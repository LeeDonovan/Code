module Bank

type Account =
  | Balance of int
  | Overdrawn of int
  | Empty

// type Password = string

// type Name = string

// type Customer =
//     { Name: Name
//       Password: Password
//       Account: Account }

// type Action =
//     | Withdraw of int
//     | Deposit of int

// type Session =
//     | Valid of Customer
//     | BadPassword

// type TransactionResult =
//     | AccountUpdated of Customer
//     | Failed
// let makeAccount()  = Account
//     new Account with
//       member this.Empty = ()
//   }

let makeAccount () = Empty


//let withdraw amt acc =
  //match acc with
    //| Balance b -> Balance
    //| Overdrawn od -> Overdrawn
    //| Empty


// let makeCustomer nam pass =
//   {
//     Name = nam
//     Password = pass
//     Account = makeAccount()
//   }

//let deposit (x : int, a : Account) =
//  match a with
//  | Balance a -> Balance(x + a)
 // | Empty -> Empty

let deposit (x : int, a : Account) = 
  match (a) with 
  | Balance a -> Balance(x + a)
  | Empty -> Empty

//let Balance num =


// let makeSession pass Customer =
//   {
//     if pass = makeCustomer.Password then
//       Valid Customer
//     else
//       BadPassword
//   }
// let performTransaction Action Session =
//   match Action with
//     | deposit d ->
//       match Session with
//         | Valid


