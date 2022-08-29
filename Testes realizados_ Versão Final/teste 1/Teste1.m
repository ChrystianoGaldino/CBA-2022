
                              %%%%Referências%%%%
% https://www.mathworks.com/matlabcentral/answers/108616-plotting-data-from-a-csv-file
%https://lrodrigo.sgs.lncc.br/wp/programacao/matlab-exemplos-de-codigos-para-geracao-de-graficos/


% Chrystiano Alves Galdino
% PPGEE
% LCCE

%__________________________________________________________________________%

%Leitura dos dados
%Caso Base
Array=csvread('CB.csv'); %leitura do arquivo
col1 = Array(:, 1);  %armazena a coluna 1 - tempo(s)
col2 = Array(:, 2);  %armazena a coluna 2 - módulo de VF
col5 = Array(:, 5);  %armazena a coluna 5 - VF
col6 = Array(:, 6);  %armazena a coluna 6 - corrente
col7 = Array(:, 7);  %armazena a coluna 7 - FP
col8 = Array(:, 8);  %armazena a coluna 8 - Potência Ativa
col9 = Array(:, 9);  %armazena a coluna 9 - Potência Aparente

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
% 
% %%%%%%%%% Caso 10 x Rs %%%%%%%%%

Array=csvread('10xRs.csv'); %leitura do arquivo
col1a = Array(:, 1);  %armazena a coluna 1 - tempo(s)
col2a = Array(:, 2);  %armazena a coluna 2 - módulo de VF
col5a = Array(:, 5);  %armazena a coluna 5 - VF
col6a = Array(:, 6);  %armazena a coluna 6 - corrente
col7a = Array(:, 7);  %armazena a coluna 7 - FP
col8a = Array(:, 8);  %armazena a coluna 8 - Potência Ativa
col9a = Array(:, 9);  %armazena a coluna 9 - Potência Aparente


% %gráfico do módulo de VF
% figure (6);
% plot(col1a, col2a,'r')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('Módulo de VF');
% %ylim([0 250])
% legend('Tensão VF')
% grid on;
% 
% %gráfico de corrente
% figure (7);
% plot(col1a, col6a,'b')
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
% figure (8);
% plot(col1a, -col7a,'k')
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
% figure (9);
% plot(col1a, -col8a,'k','LineWidth',2)
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
% figure (10);
% plot(col1a, col9a,'m')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('S');
% %ylim([0 3000])
% % ax = gca;
% % ax.FontSize = 16;
% legend('Potência Aparente')
% grid on;
% 
% 
% %%%%%%%%% Caso 10 x Ls %%%%%%%%%

Array=csvread('10xLs.csv'); %leitura do arquivo
col1b = Array(:, 1);  %armazena a coluna 1 - tempo(s)
col2b = Array(:, 2);  %armazena a coluna 2 - módulo de VF
col5b = Array(:, 5);  %armazena a coluna 5 - VF
col6b = Array(:, 6);  %armazena a coluna 6 - corrente
col7b = Array(:, 7);  %armazena a coluna 7 - FP
col8b = Array(:, 8);  %armazena a coluna 8 - Potência Ativa
col9b = Array(:, 9);  %armazena a coluna 9 - Potência Aparente


% %gráfico do módulo de VF
% figure (11);
% plot(col1b, col2b,'r')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('Módulo de VF');
% %ylim([0 250])
% legend('Tensão VF')
% grid on;
% 
% %gráfico de corrente
% figure (12);
% plot(col1b, col6b,'b')
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
% figure (13);
% plot(col1b, -col7b,'k')
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
% figure (14);
% plot(col1b, -col8b,'k','LineWidth',2)
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
% figure (15);
% plot(col1b, col9b,'m')
% title ('Gráfico de Descarga - CB');
% xlabel ('tempo (s)');
% ylabel ('S');
% %ylim([0 3000])
% % ax = gca;
% % ax.FontSize = 16;
% legend('Potência Aparente')
% grid on;



%%%Variaveis do tamanho das letras ########
L1 = 20;
L2 = 14;
L3 = 16;



%%%%%%%  subplot VF %%%%%%
figure (21);

subplot(4,1,1);
 plot(col1, col2,'r',col1a,col2a,'k',col1b,col2b,'b','LineWidth',2)
 title ('Gráfico de Descarga','FontSize', L1);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('VF (V)','FontSize', L1);
 legend('VF - CB', 'VF - 10x Rs','VF - 10x Ls','FontSize', L2)
 ylim([140 170])
%ylim([150 180])

ax = gca;
ax.FontSize = L3;
grid on;

subplot(4,1,2); 
 plot(col1, -col7,'r',col1a,-col7a,'k',col1b,-col7b,'b','LineWidth',2)
% title ('Gráfico de Descarga','FontSize', 28);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('FP','FontSize', L1);
 legend('FP - CB', 'FP - 10x Rs','FP - 10x Ls','FontSize', L2)
 ylim([0.9 1])
 %ylim([150 180])

ax = gca;
ax.FontSize = L3;
grid on;

subplot(4,1,3); 
 plot(col1, -col8,'r',col1a,-col8a,'k',col1b,-col8b,'b','LineWidth',2)
 %title ('Gráfico de Descarga','FontSize', 28);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('P (W)','FontSize', L1);
 legend('P - CB', 'P - 10x Rs','P - 10x Ls','FontSize', L2)
 %ylim([0.92 0.98])
 ylim([1300 1800])

ax = gca;
ax.FontSize = L3;
grid on;

subplot(4,1,4); 
 plot(col1, (sqrt(3)*(col9).*sin(acos(col7))),'r',col1a,(sqrt(3)*(col9a).*sin(acos(col7a))),'k',col1b,(sqrt(3)*(col9b).*sin(acos(col7b))),'b','LineWidth',2)
 %title ('Gráfico de Descarga','FontSize', 28);
 xlabel ('tempo (s)','FontSize', L1);
 ylabel ('Q (VAR)','FontSize', L1);
 legend('Q - CB', 'Q - 10x Rs','Q - 10x Ls','FontSize', L2)
 %ylim([0.92 0.98])
 ylim([400 600])

ax = gca;
ax.FontSize = L3;
grid on;

% subplot(4,1,4); 
%  plot(col1, (col9.*sin(acos(col7))),'r','LineWidth',2)
%  %title ('Gráfico de Descarga','FontSize', 28);
%  xlabel ('tempo (s)','FontSize', L1);
%  ylabel ('Potência Reativa (VAr)','FontSize', L1);
%  legend('Q - CB','FontSize', L2)
%  %ylim([0.92 0.98])
%  %ylim([150 180])
% 
% ax = gca;
% ax.FontSize = L3;
% grid on;
