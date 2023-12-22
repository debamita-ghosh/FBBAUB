clear; clc;
Expt = 1;
T1= [50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000];
sigma = 5;
runs = 10000;
t_inv = tinv(0.975, runs-1);

A = [80 100];

conf_prob_our = zeros(numel(A),numel(T1));
uconf_prob_our = zeros(numel(A),numel(T1));
lconf_prob_our = zeros(numel(A),numel(T1));
conf_prob_LSE = zeros(numel(A),numel(T1));
uconf_prob_LSE = zeros(numel(A),numel(T1));
lconf_prob_LSE = zeros(numel(A),numel(T1));
conf_prob_SeqHav = zeros(numel(A),numel(T1));
uconf_prob_SeqHav = zeros(numel(A),numel(T1));
lconf_prob_SeqHav = zeros(numel(A),numel(T1));

arm_output_our = zeros(numel(A),numel(T1), runs);
arm_output_LSE = zeros(numel(A),numel(T1), runs);
arm_output_SeqHav = zeros(numel(A),numel(T1), runs);
max1 = 0;
for a=1:numel(A)
    arm = 1:A(a);    
    fileID = fopen('unimodal expt/Unimodal_Expt'+string(Expt)+'_K_'+string(A(a))+'.txt','r');
    mean = (fscanf(fileID,'%f'))';

    muR = round(mean,2);

    [~,index] = max(muR);
    Astar = arm(index);
    Astar;
    max_mean = muR(Astar);

    %%%%%% Our Algo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    L=ceil((log2(A(a))-log2(3))/(log2(3)-log2(2)));
    T1_min_our = ceil(4/L);
    for t=1:numel(T1)
        if T1(t) >= T1_min_our
            err=0;
            sum_thrpt = 0;
            prob_our_runs = zeros(1,runs);
            for num=1:runs
                arm1=arm; muR1=muR;
                Tl=0;T2=T1(t);
                for h=1:L+1
                    T2=T2-4*Tl;
                    %if numel(arm1)~=1
                    if numel(arm1)>3
                        if h==1||h==2
                            Tl=floor(T1(t)/4*2^(L-2)*3^(-L+1));
                        else
                            Tl=floor(T1(t)/4*2^(L+1-h)*3^(-L-2+h));
                        end
                        x(1)=arm1(1);x(2)=max(ceil((arm1(numel(arm1))-arm1(1))/3)+arm1(1),x(1)+1);
                        x(3)=max(floor(2*(arm1(numel(arm1))-arm1(1))/3)+arm1(1),x(2)+1);x(4)=arm1(numel(arm1));
                        mu=zeros(1,4);
                        for j=1:4
                            for k=1:Tl
                                %mu(j)= mu(j)+muR(x(j))+15*randn; %
                                mu(j)=mu(j)+ muR(x(j))+sigma*randn;
                            end
                                mu(j)=mu(j)/Tl;
                        end
                        if (mu(1)>=mu(3)&&mu(1)>=mu(4))||(mu(2)>=mu(3)&&mu(2)>=mu(4))
                            arm1=x(1):x(3);
                            muR1=muR(x(1):x(3));
                        else
                            arm1=x(2):x(4);
                            muR1=muR(x(2):x(4));
                        end
                    else
                        mu=zeros(1,numel(arm1));
                        x=arm1;Tl=T2/3;
                        for j=1:numel(arm1)
                            for k=1:Tl
                                %mu(j)=mu(j)+muR(x(j))+15*randn; %
                                mu(j)=mu(j)+muR(x(j))+sigma*randn;
                            end
                                mu(j)=mu(j)/Tl;
                        end      
                        [~,r]=max(mu);
                        arm1=arm1(r);
                    end
                end
                arm_output_our(a,t,num) = arm1;
                if arm_output_our(a,t,num)==Astar
                    err=err+1;
                    prob_our_runs(num) = 0;
                else
                    prob_our_runs(num) = 1;
                end
            end
            conf_prob_our(a,t) = 1- (err/runs);
            uconf_prob_our(a,t) = min(1,conf_prob_our(a,t) + (std(prob_our_runs)*t_inv)/sqrt(runs-1));
            lconf_prob_our(a,t) = max(0,conf_prob_our(a,t) - (std(prob_our_runs)*t_inv)/sqrt(runs-1));
         else
            conf_prob_our(a,t) = NaN;
            uconf_prob_our(a,t) = NaN;
            lconf_prob_our(a,t) = NaN;
        end
    end


    %%%%%% LSE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    constant = 1/log(3/2);
    L2=ceil((log2(A(a))-log2(3))/(log2(3)-log2(2)));
    T1_min_LSE = 4*L2;
    for t=1:numel(T1)
        if T1(t) >= T1_min_LSE
            err2 = 0;
            Tl2 = T1(t)/(4*(L2+1));
            sum_thrpt3 = 0;
            prob_LSE_runs = zeros(1,runs);
            mur_arm_wat_LSE = zeros(1,num);
            for num=1:runs
                arm3=arm; muR3=muR;
                T2=T1(t);
                for h=1:L2+1
                    %if numel(arm1)~=1
                    if numel(arm3)>3
                        T2=T2-4*Tl2;
                        x(1)=arm3(1);x(2)=max(ceil((arm3(numel(arm3))-arm3(1))/3)+arm3(1),x(1)+1);
                        x(3)=max(floor(2*(arm3(numel(arm3))-arm3(1))/3)+arm3(1),x(2)+1);x(4)=arm3(numel(arm3));

                        mu3=zeros(1,4);
                        for j=1:4
                            for k=1:Tl2
                                %mu(j)= mu(j)+muR(x(j))+15*randn; %
                                mu3(j)=mu3(j)+ muR(x(j))+sigma*randn;
                            end
                                mu3(j)=mu3(j)/Tl2;
                        end
                        if (mu3(1)>=mu3(3)&&mu3(1)>=mu3(4))||(mu3(2)>=mu3(3)&&mu3(2)>=mu3(4))
                            arm3=x(1):x(3);
                            muR3=muR(x(1):x(3));
                        else
                            arm3=x(2):x(4);
                            muR3=muR(x(2):x(4));
                        end
                    else
                        mu3=zeros(1,numel(arm3));
                        x=arm3;Tl4=Tl2*4/3;
                        for j=1:numel(arm3)
                            for k=1:Tl4
                                %mu(j)=mu(j)+muR(x(j))+15*randn; %
                                mu3(j)=mu3(j)+muR(x(j))+sigma*randn;
                            end
                                mu3(j)=mu3(j)/Tl4;
                        end      
                        [~,r]=max(mu3);
                        arm3=arm3(r);
                    end
                end
                arm_output_LSE(a,t,num) = arm3;        
                if arm3==Astar
                    err2=err2+1;
                    prob_LSE_runs(num) = 0;
                else
                    prob_LSE_runs(num) = 1;
                end
            end
            conf_prob_LSE(a,t) = 1- (err2/runs);
            uconf_prob_LSE(a,t) = min(1,conf_prob_LSE(a,t) + (std(prob_LSE_runs)*t_inv)/sqrt(runs-1));
            lconf_prob_LSE(a,t) = max(0,conf_prob_LSE(a,t) - (std(prob_LSE_runs)*t_inv)/sqrt(runs-1));
        else
            conf_prob_LSE(a,t) = NaN;
            uconf_prob_LSE(a,t) = NaN;
            lconf_prob_LSE(a,t) = NaN;
        end
    end
    
    %%%%%%%%% Sequential Halving %%%%%%%%
    L1=ceil(log2(A(a)));
    T1_min_SeqHav = A(a)*L1;
    for t=1:numel(T1)
        if T1(t) >= T1_min_SeqHav
            err1 = 0;
            sum_thrpt1 = 0;
            prob_seqhav_runs = zeros(1,runs);
            mur_arm_wat_seqhav = zeros(1,runs);
            for num=1:runs
                arm2=arm; muR2=muR;A1=A(a);
                for i1=1:L1
                    if A1~=1
                        Tl1=T1(t)/(A1*L1);
                        mu1=zeros(1,A1);
                        for j=1:A1
                            for k=1:Tl1
                                mu1(j)=mu1(j)+muR2(j)+sigma*randn;
                            end
                            mu1(j)=mu1(j)/Tl1;
                        end
                        hal=floor(A1/2);
                        mu2=sort(mu1);
                        arm2=arm2(mu1>mu2(hal));
                        muR2=muR2(mu1>mu2(hal));
                        A1=ceil(A1/2);
                    end
                end
                arm_output_SeqHav(a,t,num) = arm2;
                if arm_output_SeqHav(a,t,num)==Astar
                    err1=err1+1;
                    prob_seqhav_runs(num) = 0;
                else
                    prob_seqhav_runs(num) = 1;
                end
            end
            conf_prob_SeqHav(a,t) = 1- (err1/runs);
            uconf_prob_SeqHav(a,t) = min(1,conf_prob_SeqHav(a,t) + (std(prob_seqhav_runs)*t_inv)/sqrt(runs-1));
            lconf_prob_SeqHav(a,t) = max(0,conf_prob_SeqHav(a,t) - (std(prob_seqhav_runs)*t_inv)/sqrt(runs-1));              
        else
            conf_prob_SeqHav(a,t) = NaN;
            uconf_prob_SeqHav(a,t) = NaN;
            lconf_prob_SeqHav(a,t) = NaN;
       end
   end
end
writematrix(conf_prob_our(1,:), 'proberr/our/conf_prob_our_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_our(1,:), 'proberr/our/lconf_prob_our_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_our(1,:), 'proberr/our/uconf_prob_our_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');

writematrix(conf_prob_our(2,:), 'proberr/our/conf_prob_our_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_our(2,:), 'proberr/our/lconf_prob_our_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_our(2,:), 'proberr/our/uconf_prob_our_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');

writematrix(conf_prob_LSE(1,:), 'proberr/LSE/conf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_LSE(1,:), 'proberr/LSE/lconf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_LSE(1,:), 'proberr/LSE/uconf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');

writematrix(conf_prob_LSE(2,:), 'proberr/LSE/conf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_LSE(2,:), 'proberr/LSE/lconf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_LSE(2,:), 'proberr/LSE/uconf_prob_LSE_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');

writematrix(conf_prob_SeqHav(1,:), 'proberr/SeqHalv/conf_prob_SeqHav_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_SeqHav(1,:), 'proberr/SeqHalv/lconf_prob_SeqHav_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_SeqHav(1,:), 'proberr/SeqHalv/uconf_prob_SeqHav_Expt'+string(Expt)+'_K_'+str(A(1))+'.txt', 'Delimiter', 'tab');

writematrix(conf_prob_SeqHav(2,:), 'proberr/SeqHalv/conf_prob_SeqHalv_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(lconf_prob_SeqHav(2,:), 'proberr/SeqHalv/lconf_prob_SeqHalv_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');
writematrix(uconf_prob_SeqHav(2,:), 'proberr/SeqHalv/uconf_prob_SeqHalv_Expt'+string(Expt)+'_K_'+str(A(2))+'.txt', 'Delimiter', 'tab');