# ------------------------------循环计算comsol-----------
inputcomsolstr0 = """


function out = model
%
% test1.m
%
% Model exported on Jan 24 2022, 11:20 by COMSOL 5.6.0.280.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath('I:\Desktop');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 2);

model.component('comp1').mesh.create('mesh1');

model.component('comp1').physics.create('spf', 'LaminarFlow', 'geom1');
model.component('comp1').physics.create('tds', 'DilutedSpecies', {'c'});

model.param().set("U_mean", "0.00012[m/s]", "Mean inflow velocity");
model.param().set("L", "0.0005[m]", "Height");
model.param().set("W", "0.001[m]", "Width");
model.param().set("R", "0.0001[m]", "Cylinder radius");


model.component('comp1').geom('geom1').lengthUnit('cm');
model.component("comp1").geom("geom1").create("imp1", "Import");
model.component("comp1").geom("geom1").feature("imp1").set("filename", "D:\\2DFlow\\Untitled.mphbin");
model.component('comp1').geom('geom1').run;

model.component('comp1').common.create('free1', 'DeformingDomainDeformedGeometry');
model.component('comp1').common('free1').selection.all;
model.component('comp1').common('free1').selection.set([1]);
model.component('comp1').common('free1').set('smoothingType', 'laplace');
model.component('comp1').common.create('pnmv1', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv1').selection.set([11 12 21 22 25 26 35 36 49 50 59 60 73 74 83 84 91 92 101 102 105 106 115 116 133 134 143 144 147 148 157 158 171 172 181 182 185 186 195 196]);
model.component('comp1').common('pnmv1').set('prescribedNormalVelocity', '0.0000369*(3.78267E-06+8.53118E-04*abs(H))*(1-10^(SIcal))+0.00012804*1.55543E-11*(1-10^(SIpyr))');

model.component('comp1').common.create('pnmv2', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv2').selection.set([9 10 19 20 33 34 43 44 47 48 57 58 71 72 81 82 85 86 95 96 107 108 117 118 131 132 141 142 145 146 155 156 173 174 183 184 187 188 197 198]);
model.component('comp1').common('pnmv2').set('prescribedNormalVelocity', '0.00010079*(1.4918E-12+9.629E-8*(abs(H)^1.5))*(1-10^(SIano))+0.00012804*1.55543E-11*(1-10^(SIpyr))');

model.component('comp1').common.create('pnmv3', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv3').selection.set([7 8 17 18 31 32 41 42 45 46 55 56 69 70 79 80 93 94 103 104 109 110 119 120 125 126 135 136 153 154 163 164 169 170 179 180 193 194 203 204]);
model.component('comp1').common('pnmv3').set('prescribedNormalVelocity', '0.00015616*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))+0.00012804*1.55543E-11*(1-10^(SIpyr))');

model.component('comp1').common.create('pnmv4', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv4').selection.set([5 6 15 16 29 30 39 40 53 54 63 64 67 68 77 78 87 88 97 98 113 114 123 124 129 130 139 140 151 152 161 162 167 168 177 178 189 190 199 200]);
model.component('comp1').common('pnmv4').set('prescribedNormalVelocity', '0.00002269*2.86362E-13*(1-10^(SIqua))+0.00012804*1.55543E-11*(1-10^(SIpyr))');

model.component('comp1').common.create('pnmv5', 'PrescribedNormalMeshVelocityDeformedGeometry');
model.component('comp1').common('pnmv5').selection.set([13 14 23 24 27 28 37 38 51 52 61 62 65 66 75 76 89 90 99 100 111 112 121 122 127 128 137 138 149 150 159 160 165 166 175 176 191 192 201 202]);
model.component('comp1').common('pnmv5').set('prescribedNormalVelocity', '0.00012804*1.55543E-11*(1-10^(SIpyr))');

% 插值
model.func.create('int1', 'Interpolation');
model.func.create('int2', 'Interpolation');
model.func.create('int3', 'Interpolation');
model.func.create('int4', 'Interpolation');

%插值1-1
model.func('int1').model('comp1');
model.func('int1').set('funcs', {'intAl' '1'; 'intCO3' '2'; 'intCa' '3'; 'intCl' '4'; 'intFe2' '5'; 'intK' '6'; 'intMg' '7'; 'intNa' '8'; 'intSO4' '9'; 'intSi' '10'; 'SIcal' '11'; 'SIqua' '12'; 'SImon' '13'; 'SIpyr' '14'; 'SIano' '15'; 'inH' '16'});
model.func('int1').set('nargs', '2');
model.func('int1').set('argunit', 'm');
model.func('int1').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\initconi.txt');
model.func('int1').set('source', 'file');
model.func('int1').set('fununit', 'mol/m^3');
model.func('int1').set('defvars', 'on');

%插值1-2



%插值2
model.func('int2').model('comp1');
model.func('int2').set('argunit', 'm');
model.func('int2').set('defvars', 'on');
model.func('int2').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/Pressurei.txt');
model.func('int2').set('source', 'file');
model.func('int2').set('funcs', {'intp' '1'});
model.func('int2').set('fununit', 'Pa');
model.func('int2').set('nargs', '2');

%插值3
model.func('int3').model('comp1');
model.func('int3').set('argunit', 'm');
model.func('int3').set('defvars', 'on');
model.func('int3').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/flowvelocityi.txt');
model.func('int3').set('source', 'file');
model.func('int3').set('funcs', {'intu' '1'; 'intv' '2'});
model.func('int3').set('fununit', 'm/s');
model.func('int3').set('nargs', '2');

%插值4
model.func('int4').model('comp1');
model.func('int4').set('argunit', 'm');
model.func('int4').set('defvars', true);
model.func("int4").set("frame", "mesh");
model.func('int4').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocityi.txt');
model.func('int4').set('source', 'file');
model.func('int4').set('funcs', {'materialu' '1'; 'materialv' '2'});
model.func('int4').set('fununit', 'm');
model.func('int4').set('nargs', '2');

model.component("comp1").common("free1").set('initialDeformation', {'materialu', 'materialv', '0'});

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('density', {'1'});
model.component('comp1').material('mat1').propertyGroup('def').set('dynamicviscosity', {'3e-3'});

model.component('comp1').physics('spf').create('inl1', 'InletBoundary', 1);
model.component('comp1').physics('spf').create('out1', 'OutletBoundary', 1);
model.component('comp1').physics('spf').feature('inl1').selection.set([1]);
model.component('comp1').physics('spf').feature('out1').selection.set([4]);
model.component("comp1").physics("spf").feature("init1").set('u_init', {'intu' 'intv' '0'});
model.component("comp1").physics("spf").feature("init1").set('p_init', 'intp');
model.component("comp1").physics("spf").feature("inl1").set("ComponentWise", "VelocityFieldComponentWise");
model.component("comp1").physics("spf").feature("inl1").set('u0', {'0.00012' '0' '0'});
model.component("comp1").physics("spf").feature("inl1").set("BoundaryCondition", "Velocity");


model.component('comp1').physics('tds').feature('cdm1').set('u_src', 'root.comp1.u');
model.component("comp1").physics("tds").field("concentration").component(1, "H");
model.component("comp1").physics("tds").field("concentration").component(2, "Ca");
model.component("comp1").physics("tds").field("concentration").component(3, "C");
model.component("comp1").physics("tds").field("concentration").component(4, "Al");
model.component("comp1").physics("tds").field("concentration").component(5, "Na");
model.component("comp1").physics("tds").field("concentration").component(6, "K");
model.component("comp1").physics("tds").field("concentration").component(7, "Fe");
model.component("comp1").physics("tds").field("concentration").component(8, "Mg");
model.component("comp1").physics("tds").field("concentration").component(9, "SO4");
model.component("comp1").physics("tds").field("concentration").component(10, "Si");
model.component("comp1").physics("tds").field("concentration").component(11, "Cl");
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intCO3', 2);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intCa', 1);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intAl', 3);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intNa', 4);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intK', 5);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intFe2', 6);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intMg', 7);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intSO4', 8);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intSi', 9);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'inH', 0);
model.component("comp1").physics("tds").feature("init1").setIndex("initc", 'intCl', 10);
model.component('comp1').physics('tds').create('out1', 'Outflow', 1);
model.component('comp1').physics('tds').feature('out1').selection.set([4]);
model.component('comp1').physics('tds').create('in1', 'Inflow', 1);
model.component("comp1").physics("tds").feature("in1").selection().set(1);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 28.7, 1);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0174, 3);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 489, 4);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0213, 5);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.0733, 6);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.00452, 7);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 2.04E-4, 8);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.544, 9);
model.component("comp1").physics("tds").feature("in1").set("BoundaryConditionType", "ConcentrationConstraint");
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 0.316, 0);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 516, 10);
model.component("comp1").physics("tds").feature("in1").setIndex("c0", 950, 2);

model.component('comp1').physics('tds').create('fl1', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl1').selection.set([11 12 21 22 25 26 35 36 49 50 59 60 73 74 83 84 91 92 101 102 105 106 115 116 133 134 143 144 147 148 157 158 171 172 181 182 185 186 195 196]);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 1);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 2);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 3);
model.component("comp1").physics("tds").feature("fl1").setIndex("species", true, 9);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "-(3.78267E-06+8.53118E-04*abs(H))*(1-10^(SIcal))-6*1.55543E-11*(1-10^(SIpyr))", 0);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "(3.78267E-06+8.53118E-04*abs(H))*(1-10^(SIcal))", 1);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "(3.78267E-06+8.53118E-04*abs(H))*(1-10^(SIcal))", 2);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "2*1.55543E-11*(1-10^(SIpyr))", 3);
model.component("comp1").physics("tds").feature("fl1").setIndex("J0", "4*1.55543E-11*(1-10^(SIpyr))", 9);

model.component('comp1').physics('tds').create('fl2', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl2').selection.set([9 10 19 20 33 34 43 44 47 48 57 58 71 72 81 82 85 86 95 96 107 108 117 118 131 132 141 142 145 146 155 156 173 174 183 184 187 188 197 198]);
model.component("comp1").physics("tds").feature("fl2").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl2").setIndex("species", true, 1);
model.component("comp1").physics("tds").feature("fl2").setIndex("species", true, 3);
model.component("comp1").physics("tds").feature("fl2").setIndex("species", true, 9);
model.component("comp1").physics("tds").feature("fl2").setIndex("J0", "-8*(1.4918E-12+9.629E-8*(abs(H)^1.5))*(1-10^(SIano))-6*1.55543E-11*(1-10^(SIpyr))", 0);
model.component("comp1").physics("tds").feature("fl2").setIndex("J0", "(1.4918E-12+9.629E-8*(abs(H)^1.5))*(1-10^(SIano))", 1);
model.component("comp1").physics("tds").feature("fl2").setIndex("J0", "2*(1.4918E-12+9.629E-8*(abs(H)^1.5))*(1-10^(SIano))+2*1.55543E-11*(1-10^(SIpyr))", 3);
model.component("comp1").physics("tds").feature("fl2").setIndex("J0", "2*(1.4918E-12+9.629E-8*(abs(H)^1.5))*(1-10^(SIano))+4*1.55543E-11*(1-10^(SIpyr))", 9);

model.component('comp1').physics('tds').create('fl3', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl3').selection.set([7 8 17 18 31 32 41 42 45 46 55 56 69 70 79 80 93 94 103 104 109 110 119 120 125 126 135 136 153 154 163 164 169 170 179 180 193 194 203 204]);
model.component("comp1").physics("tds").feature("fl3").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl3").setIndex("species", true, 1);
model.component("comp1").physics("tds").feature("fl3").setIndex("species", true, 3);
model.component("comp1").physics("tds").feature("fl3").setIndex("species", true, 7);
model.component("comp1").physics("tds").feature("fl3").setIndex("species", true, 9);
model.component("comp1").physics("tds").feature("fl3").setIndex("J0", "-6*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))-6*1.55543E-11*(1-10^(SIpyr))", 0);
model.component("comp1").physics("tds").feature("fl3").setIndex("J0", "0.165*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))", 1);
model.component("comp1").physics("tds").feature("fl3").setIndex("J0", "1.67*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))+2*1.55543E-11*(1-10^(SIpyr))", 3);
model.component("comp1").physics("tds").feature("fl3").setIndex("J0", "4*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))+4*1.55543E-11*(1-10^(SIpyr))", 9);
model.component("comp1").physics("tds").feature("fl3").setIndex("J0", "0.33*(6.27486E-13+2.47084E-11*(abs(H)^0.34))*(1-10^(SImon))", 7);

model.component('comp1').physics('tds').create('fl4', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl4').selection.set([5 6 15 16 29 30 39 40 53 54 63 64 67 68 77 78 87 88 97 98 113 114 123 124 129 130 139 140 151 152 161 162 167 168 177 178 189 190 199 200]);
model.component("comp1").physics("tds").feature("fl4").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl4").setIndex("species", true, 3);
model.component("comp1").physics("tds").feature("fl4").setIndex("species", true, 9);
model.component("comp1").physics("tds").feature("fl4").setIndex("J0", "2*1.55543E-11*(1-10^(SIpyr))", 0);
model.component("comp1").physics("tds").feature("fl4").setIndex("J0", "2*1.55543E-11*(1-10^(SIpyr))", 3);
model.component("comp1").physics("tds").feature("fl4").setIndex("J0", "2.86362E-13*(1-10^(SIqua))+4*1.55543E-11*(1-10^(SIpyr))", 9);

model.component('comp1').physics('tds').create('fl5', 'FluxBoundary', 1);
model.component('comp1').physics('tds').feature('fl5').selection.set([13 14 23 24 27 28 37 38 51 52 61 62 65 66 75 76 89 90 99 100 111 112 121 122 127 128 137 138 149 150 159 160 165 166 175 176 191 192 201 202]);
model.component("comp1").physics("tds").feature("fl5").setIndex("species", true, 0);
model.component("comp1").physics("tds").feature("fl5").set("IncludeConvection", false);
model.component("comp1").physics("tds").feature("fl5").setIndex("species", true, 3);
model.component("comp1").physics("tds").feature("fl5").setIndex("species", true, 9);
model.component("comp1").physics("tds").feature("fl5").setIndex("J0", "-6*1.55543E-11*(1-10^(SIpyr))", 0);
model.component("comp1").physics("tds").feature("fl5").setIndex("J0", "2*1.55543E-11*(1-10^(SIpyr))", 3);
model.component("comp1").physics("tds").feature("fl5").setIndex("J0", "4*1.55543E-11*(1-10^(SIpyr))", 9);


model.component('comp1').mesh('mesh1').contribute('physics/spf', true);
model.component('comp1').mesh('mesh1').contribute('physics/tds', true);
model.component('comp1').mesh('mesh1').contribute('common/free1', true);
model.component('comp1').mesh('mesh1').autoMeshSize(3);
model.component('comp1').mesh('mesh1').run;

model.study.create('std1');
model.study('std1').create('time', 'Transient');
model.study('std1').feature('time').activate('spf', true);
model.study('std1').feature('time').activate('tds', true);
model.study('std1').feature('time').activate('free1', true);



model.sol.create('sol1');
model.sol('sol1').study('std1');
model.sol('sol1').attach('std1');
model.sol('sol1').create('st1', 'StudyStep');
model.sol('sol1').create('v1', 'Variables');
model.sol('sol1').create('t1', 'Time');
model.sol('sol1').feature('t1').create('fc1', 'FullyCoupled');
model.sol('sol1').feature('t1').create('d1', 'Direct');
model.sol('sol1').feature('t1').feature.remove('fcDef');

model.study('std1').feature('time').set('tlist', 'range(###)');

model.sol('sol1').attach('std1');
model.sol('sol1').feature('t1').set('tlist', 'range(###)');
model.sol("sol1").feature("t1").set("plot", "off");
model.sol("sol1").feature("t1").set("probesel", "all");
model.sol("sol1").feature("t1").set("probefreq", "tsteps");
model.sol("sol1").feature("t1").set("rtol", 0.005);
model.sol("sol1").feature("t1").set("atolglobalmethod", "scaled");
model.sol("sol1").feature("t1").set("atolglobalfactor", 0.05);
model.sol("sol1").feature("t1").set("atolglobalvaluemethod", "factor");
model.sol("sol1").feature("t1").set("endtimeinterpolation", true);
model.sol("sol1").feature("t1").set("estrat", "exclude");
model.sol("sol1").feature("t1").set("maxorder", 2);
model.sol("sol1").feature("t1").set("stabcntrl", true);
model.sol("sol1").feature("t1").set("bwinitstepfrac", "0.01");
model.sol("sol1").feature("t1").set("control", "time");
model.sol('sol1').runAll;


model.result.export.create('data2', 'Data');
model.result.export.create('data3', 'Data');
model.result.export.create('data4', 'Data');
model.result.export.create('data5', 'Data');


model.result.export('data2').set('timeinterp', 'on');
model.result.export('data2').set('unit', {' ' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L' 'mol/L'});
model.result.export('data2').set('descr', {'pH' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data2').set('expr', {'-log10(abs(H/1000))' 'Ca' 'C' 'Al' 'Na' 'K' 'Fe' 'Mg' 'SO4' 'Si' 'Cl' 'Fe' 'Mg' 'SO4' 'Si' 'Cl'});
model.result.export('data2').set('t', '#');
model.result.export('data2').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\outcono.txt');

model.result.export('data3').set('descr', {'Pressure'});
model.result.export('data3').set('timeinterp', 'on');
model.result.export('data3').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/Pressureo.txt');
model.result.export('data3').set('unit', {'Pa'});
model.result.export('data3').set('t', '#');
model.result.export('data3').set('expr', {'abs(p)'});

model.result.export('data4').set('descr', {'flow velocity'});
model.result.export('data4').set('timeinterp', 'on');
model.result.export('data4').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/flowvelocityo.txt');
model.result.export('data4').set('unit', {'m/s' 'm/s'});
model.result.export('data4').set('t', '#');
model.result.export('data4').set('expr', {'u' 'v'});

model.result.export('data5').set('descr', {'material velocity'});
model.result.export('data5').set('timeinterp', 'on');
model.result.export('data5').set('filename', 'F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result/materialvelocityo.txt');
model.result.export('data5').set('unit', {'m' 'm'});
model.result.export('data5').set('t', '#');
model.result.export('data5').set('expr', {'material.u' 'material.v'});


model.result.export('data2').run
model.result.export('data3').run
model.result.export('data4').run
model.result.export('data5').run

mphmesh(model)
ModelUtil.showProgress(true);
model.save('F:\(Comsol+Phreeqc)python\COMSOL_phreeqc\Result\model_o')

out = model;


     """