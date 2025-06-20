// src/components/FilterSidebar.jsx
import { useState } from 'react';
import axios from 'axios';

function FilterSidebar({ onFilter }) {
  const [selectedSites, setSelectedSites] = useState([]);
  const [keyword, setKeyword] = useState('');
  const [limpando, setLimpando] = useState(false);

  const toggleSite = (site) => {
    setSelectedSites((prev) =>
      prev.includes(site)
        ? prev.filter((s) => s !== site)
        : [...prev, site]
    );
  };

  const aplicarFiltros = () => {
    onFilter({
      sites: selectedSites,
      keyword: keyword.trim(),
    });
  };

  const limparBanco = async () => {
    if (!window.confirm('Deseja realmente limpar TODAS as vagas do banco?')) return;

    setLimpando(true);
    try {
      const response = await axios.post('http://localhost:8000/api/limpar-vagas/');
      alert('🧹 Banco limpo com sucesso!');
      console.log(response.data);
    } catch (error) {
      console.error('Erro ao limpar banco:', error);
      alert('❌ Erro ao limpar banco. Veja o console.');
    } finally {
      setLimpando(false);
    }
  };

  const sitesDisponiveis = [
    'Gupy',
    'InfoJobs',
    'Programathor',
    'RemoteOK',
    'Vagas.com',
    'Remotar',
  ];

  return (
    <aside className="bg-[#13293D] text-white w-64 p-4 mt-6 ml-6 mb-6 rounded-xl shadow-md space-y-6 self-start">
      <div>
        <h2 className="text-lg font-semibold mb-2">Filtros</h2>
        <div className="space-y-2">
          {sitesDisponiveis.map((site) => (
            <label key={site} className="flex items-center gap-2">
              <input
                type="checkbox"
                className="accent-[#1B98E0]"
                checked={selectedSites.includes(site)}
                onChange={() => toggleSite(site)}
              />
              {site}
            </label>
          ))}
        </div>
      </div>

      <div>
        <h3 className="text-sm font-semibold mb-2">Filtrar por palavra-chave</h3>
        <input
          type="text"
          placeholder="Ex: React, Python"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          className="w-full px-3 py-2 rounded-md text-black"
        />
      </div>

      <button
        onClick={aplicarFiltros}
        className="w-full bg-[#006494] hover:bg-[#247BA0] text-white font-medium py-2 rounded-md"
      >
        Aplicar filtros
      </button>

      <button
        onClick={limparBanco}
        disabled={limpando}
        className={`w-full mt-2 bg-red-600 hover:bg-red-700 text-white font-medium py-2 rounded-md ${
          limpando ? 'opacity-50 cursor-not-allowed' : ''
        }`}
      >
        {limpando ? 'Limpando...' : 'Limpar banco'}
      </button>
    </aside>
  );
}

export default FilterSidebar;
