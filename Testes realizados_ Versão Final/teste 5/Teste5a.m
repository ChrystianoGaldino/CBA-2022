
                              %%%%Referências%%%%
% https://www.mathworks.com/matlabcentral/answers/108616-plotting-data-from-a-csv-file
%https://lrodrigo.sgs.lncc.br/wp/programacao/matlab-exemplos-de-codigos-para-geracao-de-graficos/


% Chrystiano Alves Galdino
% PPGEE
% LCCE

%__________________________________________________________________________%

% %%%%%%%%% Teste 5a - variação de Q(ind) para Q(cap) em carga %%%%%%%%%

Array=csvread('teste5a.csv'); %leitura do arquivo
col1 = Array(:, 1);  %armazena a coluna 1 - tempo(s)
col2 = Array(:, 2);  %armazena a coluna 2 - módulo de VF
col5 = Array(:, 5);  %armazena a coluna 5 - VF
col6 = Array(:, 6);  %armazena a coluna 6 - corrente
col7 = Array(:, 7);  %armazena a coluna 7 - FP
col8 = Array(:, 8);  %armazena a coluna 8 - Potência Ativa
col9 = Array(:, 9);  %armazena a coluna 9 - Potência Aparente
% 
% 
% 
% %gráfico do módulo de VF
% figure (1);
% plot(col1, col2,'r')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('Módulo de VF');
% %ylim([0 250])
% legend('Tensão VF')
% grid on;
% 
% %gráfico de corrente
% figure (2);
% plot(col1, col6,'b')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('Corrente');
% ylim([0 15])
% % ax = gca;
% % ax.FontSize = 16;
% legend('Corrente')
% grid on;
% 
% %gráfico de FP
% figure (3);
% plot(col1, -col7,'k')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('FP');
% %ylim([0.7 1])
% % ax = gca;
% % ax.FontSize = 16;
% legend('FP')
% grid on;
% 
% %gráfico de Potência Ativa
% figure (4);
% plot(col1, -col8,'k','LineWidth',2)
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('P');
% %ylim([0 3000])
% % ax = gca;
% % ax.FontSize = 16;
% legend('Potência Ativa')
% grid on;
% 
% %gráfico de Potência Aparente
% figure (5);
% plot(col1, col9,'m')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('S');
% %ylim([0 3000])
% % ax = gca;
% % ax.FontSize = 16;
% legend('Potência Aparente')
% grid on;
% 

%%%Variaveis do tamanho das letras ########
L1 = 20;
L2 = 14;
L3 = 14;


%%%%%%%  subplot VF %%%%%%
figure (21);

subplot(4,1,1);
 plot(col1, col2,'r','LineWidth',2)
 title ('Gráfico de Carga - Variação de Q indutivo para capacitivo','FontSize', L1);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('VF (V)','FontSize', L1);
 legend('Módulo de VF','FontSize',L2)
 ylim([150 160])
%ylim([150 180])

ax = gca;
ax.FontSize = L3;
grid on;

subplot(4,1,2); 
 plot(col1, abs(col7),'k','LineWidth',2)
 %title ('Gráfico de Descarga - CB com variação de Q','FontSize', L1);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('FP','FontSize', L1);
 legend('Fator de Potência','FontSize', L2)
  ylim([0.6 1])
 %ylim([150 180])

ax = gca;
ax.FontSize = L3;
grid on;

%  subplot(4,1,3); 
%  plot(col1, col9,'b','LineWidth',2)
% % title ('Gráfico de Descarga - CB com variação de Q','FontSize', L1);
%  xlabel ('tempo (s)','FontSize', L1);
%  ylabel ('S','FontSize', L1);
%  legend('Potência Aparente (VA)','FontSize', L2)
%   %ylim([0.92 0.98])
%  %ylim([150 180])
% 
% ax = gca;
% ax.FontSize = L3;
% grid on;

 subplot(4,1,3); 
 plot(col1,(sqrt(3)*col9.*sin(acos(col7))) ,'b','LineWidth',2)
 %title ('Gráfico de Descarga - CB com variação de Q','FontSize', L1);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('Q (VAR)','FontSize', L1);
 legend('Potência Reativa','FontSize', L2)
 ylim([400 1600])
ax = gca;
ax.FontSize = L3;
grid on;


%  subplot(4,1,4); 
%  plot(col1,col8,'g','LineWidth',2)
%  %title ('Gráfico de Descarga - CB com variação de Q','FontSize', L1);
%  xlabel ('tempo (s)','FontSize', L1);
%  ylabel ('P','FontSize', L1);
%  legend('Potência Ativa (W)','FontSize', L2)
%  ylim([1000 1500])
% 
% ax = gca;
% ax.FontSize = L3;
% grid on;


 subplot(4,1,4); 
 plot(col1, sqrt(3)*col9,'g','LineWidth',2)
% title ('Gráfico de Descarga - CB com variação de Q','FontSize', L1);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('S (VA)','FontSize', L1);
 legend('Potência Aparente','FontSize', L2)
 ylim([1200 2000])

ax = gca;
ax.FontSize = L3;
grid on;




% %%%%%%% subplot FP %%%%%%
% figure (22);
% 
% subplot(2,1,1);
% %plot(col1, col7,'r', col21, col27,'k')
% plot(col1, -1*col7,'r', col21, -1*col27,'k')
% title ('Gráfico de Carga - FP Unitário','FontSize', 28);
% xlabel ('tempo (s)','FontSize', 28);
% ylabel ('Fator de Potência','FontSize', 28);
% legend('Carga - CB', 'Carga - 10x CB','FontSize', 20)
% ylim([0 1])
% 
% ax = gca;
% ax.FontSize = 16;
% 
% grid on;
% 
% 
% subplot(2,1,2); 
% plot( col31, -1*col37,'r', col41, -1*col47,'k')
% %plot( col31, 1*col37,'r', col41, 1*col47,'k')
% title ('Gráfico de Descarga - FP Unitário','FontSize', 28);
% xlabel ('tempo (s)','FontSize', 28);
% ylabel ('Fator de Potência','FontSize', 28);
% legend('Descarga - CB', 'Descarga - 10x CB','FontSize', 20)
% %ylim([-1  -0.8])
% ylim([0 1])
% 
% ax = gca;
% ax.FontSize = 16;
% 
% grid on;
% 
% 
