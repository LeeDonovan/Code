`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/09/2020 12:26:51 AM
// Design Name: 
// Module Name: RegisterfileWithALU_tester
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module RegisterfileWithALU_tester;
    reg [5:0] Read1;
    reg [5:0] Read2;
    reg [5:0] WriteReg;
    reg [63:0] WriteData;
    reg RegWrite;
    reg clock;
    reg [1:0] ALUOp;
    reg [10:0] Opcode_field;
    wire [63:0] ALU_result;
    wire Zero;
    wire [3:0] ALU_operation;
    wire [63:0] Data1;
    wire [63:0] Data2;
    
    RegisterfileWithALU uut(
                            .Read1(Read1),
                            .Read2(Read2),
                            .WriteReg(WriteReg),
                            .WriteData(WriteData),
                           .RegWrite(RegWrite),
                            .clock(clock),
                            .ALUOp(ALUOp),
                            .Opcode_field(Opcode_field),
                            .ALU_result(ALU_result),
                            .Zero(Zero),
                            .ALU_operation(ALU_operation),
                            .Data1(Data1),
                            .Data2(Data2)
                            );
     
     
initial begin
clock = 0;
#10;

RegWrite = 1;
WriteReg <= 6'b000101;
WriteData <= 64'h5555555555555555;

#10
clock = 1;
#10

RegWrite = 1;
WriteReg <= 6'b001010;
WriteData <= 64'haaaaaaaaaaaaaaaa;
clock = 0;

#10
clock = 1;
Read1 <= 6'b000101;
Read2 <= 6'b001010;
#10

//Read1 <= 6'b000101;
//Read2 <= 6'b001010;
//correct:
//clock = 0;
//correct:
//Read1 <= 6'b000101;
//Read2 <= 6'b001010;
//ALUOp = 2'b10;

//correct:
//#10
//clock = 1;
//#10


//clock = 1;
//Read1 <= 6'b000101;
//Read2 <= 6'b001010;
//ALUOp = 2'b10;

//#10
//clock = 0;
//#10
clock=0;
ALUOp = 2'b10;
Opcode_field = 11'b10001010000;
RegWrite = 1;
WriteReg <= 6'b000001;
WriteData <= ALU_result;

#10
clock = 1;
#10

clock = 0;
Opcode_field = 11'b10101010000;
RegWrite = 1;
WriteReg <= 6'b000010;
WriteData <= ALU_result;

#10
clock = 1;
#10

clock = 0;
Opcode_field = 11'b10001011000;
RegWrite = 1;
WriteReg <= 6'b000011;
WriteData <= ALU_result;

#10
clock = 1;
#10

clock = 0;
Opcode_field = 11'b11001011000;
RegWrite = 1;
WriteReg <= 6'b000100;
WriteData <= ALU_result;
#10
clock = 1;
#10
$stop;


end

endmodule
