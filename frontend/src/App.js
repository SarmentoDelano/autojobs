import { useState } from 'react';
import Header from './components/Header';
import FilterSidebar from './components/FilterSidebar';
import JobCard from './components/JobCard';

function App() {
  const todasAsVagas = [
    // Adicione mais vagas mock se quiser testar a paginação
    {
      empresa: 'Globo',
      cargo: 'Desenvolvedor(a) Back-end',
      tags: ['Remoto', 'Python'],
      link: 'https://globo.com/vaga',
    },
    {
      empresa: 'Google',
      cargo: 'Engenheiro(a) de Software',
      tags: ['Remoto', 'React'],
      link: 'https://google.com/carreiras',
    },
    // ... mais vagas mock
  ];

  const vagasPorPagina = 30;
  const [currentPage, setCurrentPage] = useState(1);

  const totalPaginas = Math.ceil(todasAsVagas.length / vagasPorPagina);
  const startIndex = (currentPage - 1) * vagasPorPagina;
  const vagasVisiveis = todasAsVagas.slice(startIndex, startIndex + vagasPorPagina);

  const mudarPagina = (pagina) => {
    if (pagina >= 1 && pagina <= totalPaginas) {
      setCurrentPage(pagina);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-[#E8F1F2]">
      <Header />
      <div className="flex">
        <FilterSidebar />
        <main className="flex-1 p-6">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {vagasVisiveis.map((vaga, index) => (
              <JobCard
                key={index}
                empresa={vaga.empresa}
                cargo={vaga.cargo}
                tags={vaga.tags}
                link={vaga.link}
              />
            ))}
          </div>

          {/* Paginação */}
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
        </main>
      </div>
    </div>
  );
}

export default App;
