K = 100;               % 100 (No. of arms)
bestarm = 70;         % 70 (Optimal arm)
start = -312;          %   (initial start value for Expt 1 and Expt 2)
stop = -311;           %   (Stop value for Expt 1 and Expt 2)
mean_bestarm = -252;   %   (mean of best arm for Expt 1 and Expt 2)

%%%%%%%%%%% Unimodal Mean for Experiment 1 %%%%%%%%%%%%%%%%%%%%
Experiment1 = 1;
mean1 = zeros(1,K);
mean1(1) = start;
mean1(bestarm) = mean_bestarm;
mean1(K) = stop;
for k=2:K
    if k<bestarm
        mean1(k) = mean1(1) + (((k-1)*(mean1(bestarm) - mean1(1)))/(bestarm-1));
    elseif k>=bestarm
        mean1(k) = mean1(bestarm) - (((k-bestarm)*(mean1(bestarm) - mean1(K)))/(K-bestarm-1));
    end
end
writematrix(mean1, 'unimodal expt/Unimodal_Expt'+string(Experiment1)+'_K_'+string(K)+'.txt', 'Delimiter', 'tab');

%%%%%%%%%%% Unimodal Mean for Experiment 2 %%%%%%%%%%%%%%%%%%%%
Experiment2 = 2;
mean2 = zeros(1,K);
mean2(1) = start;
mean2(bestarm) = mean_bestarm;
mean2(K) = stop;
for k=2:K
    if k<bestarm
        mean2(k) = mean2(1) + (2*((k-1)*(mean2(bestarm) - mean2(1)))/((bestarm-1)));
    elseif k>=bestarm
        mean2(k) = mean2(bestarm) - (2*((k-bestarm)*(mean2(bestarm) - mean2(K)))/((K-bestarm-1)));
    end
end
writematrix(mean2, 'unimodal expt/Unimodal_Expt'+string(Experiment2)+'_K_'+string(K)+'.txt', 'Delimiter', 'tab');


%%%%%%%%%%% Unimodal Mean for Experiment 3 %%%%%%%%%%%%%%%%%%%%
Experiment1 = 3;
mean1 = zeros(1,K);
mean1(1) = start;
for k=2:K
    mean1(k) = mean1(1) - (0.6*(k-1)/(K-1));
end
writematrix(mean1, 'unimodal expt/Unimodal_Expt'+string(Experiment1)+'_K_'+string(K)+'.txt', 'Delimiter', 'tab');

%%%%%%%%%%% Unimodal Mean for Experiment 4 %%%%%%%%%%%%%%%%%%%%
Experiment2 = 4;
mean2 = zeros(1,K);
mean2(1) = start;
for k=2:K
    mean2(k) = mean2(1) - (0.01*(1+4/K)^(k));
end
writematrix(mean2, 'unimodal expt/Unimodal_Expt'+string(Experiment2)+'_K_'+string(K)+'.txt', 'Delimiter', 'tab');
