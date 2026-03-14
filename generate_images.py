import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

df = pd.read_csv('vgsales.csv')
df_clean = df.dropna(subset=['Year', 'Publisher']).copy()
df_clean['Year'] = df_clean['Year'].astype(int)

# Plot 1
platform_years = df_clean.groupby('Platform')['Year'].agg(Tahun_Rilis_Pertama='min', Tahun_Rilis_Terakhir='max')
platform_years['Umur_Pasar_(Tahun)'] = platform_years['Tahun_Rilis_Terakhir'] - platform_years['Tahun_Rilis_Pertama'] + 1
platform_sales = df_clean.groupby('Platform')['Global_Sales'].sum().reset_index()
platform_sales.rename(columns={'Global_Sales': 'Total_Penjualan_Global'}, inplace=True)
platform_analysis = pd.merge(platform_sales, platform_years, on='Platform')
top_platforms = platform_analysis.sort_values(by='Total_Penjualan_Global', ascending=False).head(10)

fig, ax1 = plt.subplots(figsize=(14, 7))
sns.barplot(x='Platform', y='Total_Penjualan_Global', data=top_platforms, color='skyblue', ax=ax1, label='Total Penjualan Global (Juta Kopi)')
ax1.set_ylabel('Total Penjualan Global (Juta Kopi)', fontsize=12, color='blue')
ax1.set_xlabel('Platform/Konsol', fontsize=12)
ax1.set_title('Top 10 Platform Sepanjang Sejarah: Penjualan Global vs Umur Pasar', fontsize=16, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
sns.lineplot(x='Platform', y='Umur_Pasar_(Tahun)', data=top_platforms, color='red', marker='o', ax=ax2, label='Umur Pasar (Tahun)', linewidth=2.5)
ax2.set_ylabel('Umur Pasar (Tahun)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.grid(False)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
plt.savefig('platform_trends.png', bbox_inches='tight')
plt.close()

# Plot 2
top5_publishers = df_clean.groupby('Publisher')['Global_Sales'].sum().nlargest(5)
top5_publisher_names = top5_publishers.index.tolist()
df_top5_pub = df_clean[df_clean['Publisher'].isin(top5_publisher_names)]
pub_genre_sales = df_top5_pub.groupby(['Publisher', 'Genre'])['Global_Sales'].sum().reset_index()

plt.figure(figsize=(16, 8))
sns.barplot(x='Publisher', y='Global_Sales', hue='Genre', data=pub_genre_sales, order=top5_publisher_names, palette='Paired')
plt.title('Strategi Monopoli Market: Penguasaan Genre oleh 5 Publisher Teratas', fontsize=16, fontweight='bold')
plt.ylabel('Total Penjualan Global (Juta Kopi)', fontsize=12)
plt.xlabel('Nama Publisher', fontsize=12)
plt.legend(title='Genre Market', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.tight_layout()
plt.savefig('publisher_strategies.png', bbox_inches='tight')
plt.close()

print("Images generated successfully.")
