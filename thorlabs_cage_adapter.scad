$fa=0.5;
$fs=0.5;
difference(){
    cube(size=[66.6, 17, 43.6]);
    translate(v=[-0.01, -0.005, 3]){
        cube(size=[10.01, 17.01, 40.61]);
    };
    translate(v=[56.61, -0.005, 3]){
        cube(size=[10.01, 17.01, 40.61]);
    };
    translate(v=[13, -0.005, -0.01]){
        cube(size=[40.6, 17.01, 36.61]);
    };
    translate(v=[13, 4.05, 0]){
        cube(size=[40.6, 8.9, 40.6]);
    };
    translate(v=[7.799999999999997, 2.5, -0.005]){
        cylinder(h=3.01, d=2.6);
    };
    translate(v=[58.8, 2.5, -0.005]){
        cylinder(h=3.01, d=2.6);
    };
    translate(v=[7.799999999999997, 14.5, -0.005]){
        cylinder(h=3.01, d=2.6);
    };
    translate(v=[58.8, 14.5, -0.005]){
        cylinder(h=3.01, d=2.6);
    };
};
