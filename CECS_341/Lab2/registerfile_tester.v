`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/04/2020 04:37:20 PM
// Design Name: 
// Module Name: registerfile_tester
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


module registerfile_tester;
reg [5:0] Read1, Read2, WriteReg;
reg [63:0] WriteData;
reg RegWrite, clock;
wire [63:0] Data1, Data2;

registerfile uut (Read1, Read2, WriteReg, WriteData, RegWrite, Data1, Data2, clock);

initial

begin

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
#10
clock = 0;

Read1 <= 6'b000101;
Read2 <= 6'b001010;

#10
$stop;


end

endmodule

