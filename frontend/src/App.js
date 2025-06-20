// src/App.js
import { useEffect, useState } from 'react';
import Header from './components/Header';
import FilterSidebar from './components/FilterSidebar';
import JobCard from './components/JobCard';
import api from './services/api';

function App() {
  const [todasAsVagas, setTodasAsVagas] = useState([]);
  const [vagasFiltradas, setVagasFiltradas] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const vagasPorPagina = 15;

  const fetchVagas = async () => {
    try {
      const response = await api.get('/vagas/');
      setTodasAsVagas(response.data);
      setVagasFiltradas(response.data); // exibir todas inicialmente
    } catch (error) {
      console.error('Erro ao buscar vagas:', error);
    }
  };

  useEffect(() => {
    fetchVagas();
  }, []);

  const aplicarFiltros = ({ sites, keyword }) => {
    const filtradas = todasAsVagas.filter((vaga) => {
      const contemSite = !sites.length || sites.includes(vaga.encontrado_em);
      const contemPalavra = !keyword || (
        vaga.cargo?.toLowerCase().includes(keyword.toLowerCase()) ||
        vaga.empresa?.toLowerCase().includes(keyword.toLowerCase()) ||
        vaga.tags?.toLowerCase().includes(keyword.toLowerCase())
      );
      return contemSite && contemPalavra;
    });

    setVagasFiltradas(filtradas);
    setCurrentPage(1);
  };

  const totalPaginas = Math.ceil(vagasFiltradas.length / vagasPorPagina);
  const startIndex = (currentPage - 1) * vagasPorPagina;
  const favoritas = vagasFiltradas.filter(v => v.favorita);
  const outras = vagasFiltradas.filter(v => !v.favorita);
  const vagasOrdenadas = [...favoritas, ...outras];
  const vagasVisiveis = vagasOrdenadas.slice(startIndex, startIndex + vagasPorPagina);


  const mudarPagina = (pagina) => {
    if (pagina >= 1 && pagina <= totalPaginas) {
      setCurrentPage(pagina);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const Paginacao = () => (
    <div className="flex justify-center mt-8 gap-2 flex-wrap">
      {Array.from({ length: totalPaginas }, (_, i) => (
        <button
          key={i}
          onClick={() => mudarPagina(i + 1)}
          className={`px-4 py-2 rounded-md text-sm font-medium ${
            currentPage === i + 1
              ? 'bg-[#006494] text-white'
              : 'bg-white text-[#13293D] border border-[#13293D]'
          }`}
        >
          {i + 1}
        </button>
      ))}
    </div>
  );

  return (
    <div className="min-h-screen bg-[#E8F1F2]">
      <Header onColetaFinalizada={fetchVagas} />
      <div className="flex">
        <FilterSidebar onFilter={aplicarFiltros} onColetaFinalizada={fetchVagas} />
        <main className="flex-1 p-6">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {vagasVisiveis.map((vaga) => (
              <JobCard
                key={vaga.id}
                id={vaga.id}
                empresa={vaga.empresa}
                cargo={vaga.cargo}
                tags={vaga.tags?.split(';')}
                link={vaga.link}
                favorita={vaga.favorita}
              />
            ))}
          </div>
          <Paginacao />
        </main>
      </div>
    </div>
  );
}

export default App;
