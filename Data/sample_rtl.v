module top (
    input wire a, b, c,
    output wire y
);
    wire n1, n2;
    and u1 (n1, a, b);
    or  u2 (n2, n1, c);
    not u3 (y, n2);
endmodule

