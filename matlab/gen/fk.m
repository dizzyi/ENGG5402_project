function FK = fk(theta1,theta2,theta3,theta4,theta5,theta6,theta7)
%FK
%    FK = FK(THETA1,THETA2,THETA3,THETA4,THETA5,THETA6,THETA7)

%    This function was generated by the Symbolic Math Toolbox version 9.0.
%    16-Dec-2021 15:37:28

t2 = cos(theta1);
t3 = cos(theta2);
t4 = cos(theta3);
t5 = cos(theta4);
t6 = cos(theta5);
t7 = cos(theta6);
t8 = cos(theta7);
t9 = sin(theta1);
t10 = sin(theta2);
t11 = sin(theta3);
t12 = sin(theta4);
t13 = sin(theta5);
t14 = sin(theta6);
t15 = sin(theta7);
t16 = theta1+theta2;
t17 = cos(t16);
t18 = sin(t16);
t19 = t4.*t6;
t20 = t4.*t13;
t21 = t5.*t11.*t13;
t22 = t11.*t12.*t14;
t25 = t5.*t6.*t11;
t23 = t5.*t17;
t24 = t5.*t18;
t26 = t4.*t12.*t17;
t27 = t6.*t11.*t17;
t28 = t6.*t12.*t17;
t29 = t4.*t12.*t18;
t30 = t11.*t13.*t17;
t31 = t6.*t11.*t18;
t32 = t12.*t13.*t17;
t33 = t6.*t12.*t18;
t34 = t11.*t13.*t18;
t35 = t12.*t13.*t18;
t36 = -t25;
t44 = t19+t21;
t37 = t19.*t23;
t38 = t20.*t23;
t39 = t19.*t24;
t40 = t20.*t24;
t41 = -t29;
t42 = -t31;
t43 = -t33;
t46 = t20+t36;
t47 = t24+t26;
t45 = -t38;
t48 = t7.*t46;
t49 = t23+t41;
t50 = t14.*t47;
t53 = t28+t34+t39;
t54 = t30+t37+t43;
t56 = t32+t40+t42;
t51 = t14.*t49;
t52 = t22+t48;
t55 = t27+t35+t45;
t57 = t7.*t53;
t58 = t7.*t54;
t59 = -t58;
t60 = t51+t57;
t61 = t50+t59;
mt1 = [-t8.*t61+t15.*t55,t8.*t60-t15.*t56,t15.*t44+t8.*t52,0.0,t7.*t47+t14.*t54,-t7.*t49+t14.*t53,t14.*t46-t7.*t11.*t12,0.0,-t8.*t55-t15.*t61,t8.*t56+t15.*t60,-t8.*t44+t15.*t52,0.0];
mt2 = [t24.*(4.8e+1./1.25e+2)+t26.*(4.8e+1./1.25e+2)-t30.*(3.3e+1./4.0e+2)-t2.*t10.*(7.9e+1./2.5e+2)-t3.*t9.*(7.9e+1./2.5e+2)+t4.*t23.*(3.3e+1./4.0e+2)-t12.*t18.*(3.3e+1./4.0e+2)-t8.*t55.*(1.07e+2./1.0e+3)-t8.*t61.*(1.1e+1./1.25e+2)+t15.*t55.*(1.1e+1./1.25e+2)-t15.*t61.*(1.07e+2./1.0e+3)-t6.*(t4.*t23-t12.*t18).*(3.3e+1./4.0e+2)];
mt3 = [t23.*(-4.8e+1./1.25e+2)+t29.*(4.8e+1./1.25e+2)-t34.*(3.3e+1./4.0e+2)+t2.*t3.*(7.9e+1./2.5e+2)-t9.*t10.*(7.9e+1./2.5e+2)+t4.*t24.*(3.3e+1./4.0e+2)+t12.*t17.*(3.3e+1./4.0e+2)+t8.*t56.*(1.07e+2./1.0e+3)+t8.*t60.*(1.1e+1./1.25e+2)-t15.*t56.*(1.1e+1./1.25e+2)+t15.*t60.*(1.07e+2./1.0e+3)-t6.*(t4.*t24+t12.*t17).*(3.3e+1./4.0e+2)];
mt4 = [t20.*(-3.3e+1./4.0e+2)+t25.*(3.3e+1./4.0e+2)-t5.*t11.*(3.3e+1./4.0e+2)-t11.*t12.*(4.8e+1./1.25e+2)-t8.*t44.*(1.07e+2./1.0e+3)+t15.*t44.*(1.1e+1./1.25e+2)+t8.*t52.*(1.1e+1./1.25e+2)+t15.*t52.*(1.07e+2./1.0e+3)+3.33e+2./1.0e+3,1.0];
FK = reshape([mt1,mt2,mt3,mt4],4,4);
