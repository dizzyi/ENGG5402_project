function T = DHT(row)

rx = Rotx(row(3));
rz = Rotz(row(4));

vx = [row(1);0;0];
vz = [0;0;row(2)];

Tz = [rz vz;0 0 0 1];
Tx = [rx vx;0 0 0 1];

T = Tz * Tx;
end