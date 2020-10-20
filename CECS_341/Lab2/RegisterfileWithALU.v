`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/09/2020 12:18:21 AM
// Design Name: 
// Module Name: RegisterfileWithALU
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


module RegisterfileWithALU(
    input [5:0] Read1,
    input [5:0] Read2,
    input [5:0] WriteReg,
    input [63:0] WriteData,
    input RegWrite,
    input clock,
    input [1:0] ALUOp,
    input [10:0] Opcode_field,
    input [63:0] A,
    input [63:0] B,
    wire [63:0] ALU_result,
    output Zero,
    wire [3:0] ALU_operation,
    wire [63:0] Data1,
    wire [63:0] Data2
    );
    
    registerfile registerfile(Read1, Read2, WriteReg, WriteData, RegWrite, Data1, Data2, clock);
    ALUwithControl ALUwithControl(ALUOp,Opcode_field,Data1,Data2,ALU_result,Zero,ALU_operation);
endmodule
